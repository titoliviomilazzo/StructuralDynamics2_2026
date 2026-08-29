"""
예제 1 — 단자유도(SDOF) 감쇠 자유진동
=====================================

m*x'' + c*x' + k*x = 0,   x(0)=x0,  x'(0)=v0

이 스크립트가 보여주려는 것은 세 가지다.

1. 단위를 변수 이름에 박고 assert로 방어하는 방식
2. 이론 해석해와 수치해(Newmark-beta)를 **나란히 계산해 서로 검증**하는 방식
3. 결과에서 감쇠비를 역산해 입력값을 복원하는 방식 (대수감쇠율)

"돌아가니까 맞겠지"가 아니라, 틀렸으면 화면에 [FAIL]이 찍히도록 짜여 있다.

실행:  python sdof_free.py
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# 1. 입력 — SI 기본단위로 통일 (kg, N, m, s)
# ---------------------------------------------------------------------------
m_kg = 1.0e5           # 질량      100 ton   = 1.0e5 kg
k_N_per_m = 4.0e6      # 강성      4,000 kN/m = 4.0e6 N/m
zeta = 0.05            # 감쇠비    5% -> 0.05 (백분율 5가 아니다)

x0_m = 0.02            # 초기변위  20 mm = 0.02 m
v0_m_per_s = 0.0       # 초기속도

n_cycles = 10          # 몇 주기까지 볼 것인가
pts_per_cycle = 200    # 한 주기당 샘플 수 (100 이상 권장)

# ---------------------------------------------------------------------------
# 2. 단위 방어선 — 틀린 단위를 넣으면 여기서 즉시 멈춘다
#    (이 3줄이 없으면 kN/m를 그대로 넣었을 때 주기가 31.6배 틀린 채 조용히 출력된다)
# ---------------------------------------------------------------------------
assert 1e3 < m_kg < 1e8, f"m_kg={m_kg}: kg 단위가 맞는가? (ton을 그대로 넣지 않았는가)"
assert 1e5 < k_N_per_m < 1e10, f"k_N_per_m={k_N_per_m}: N/m가 맞는가? (kN/m를 그대로 넣지 않았는가)"
assert 0.0 <= zeta < 1.0, f"zeta={zeta}: 저감쇠(0~1) 범위가 아니다. 5%는 0.05다"
assert abs(x0_m) < 1.0, f"x0_m={x0_m}: m 단위가 맞는가? (mm를 그대로 넣지 않았는가)"

# ---------------------------------------------------------------------------
# 3. 동특성
# ---------------------------------------------------------------------------
wn_rad_per_s = np.sqrt(k_N_per_m / m_kg)          # 고유각진동수
Tn_s = 2.0 * np.pi / wn_rad_per_s                 # 고유주기
wd_rad_per_s = wn_rad_per_s * np.sqrt(1.0 - zeta**2)  # 감쇠고유각진동수
Td_s = 2.0 * np.pi / wd_rad_per_s                 # 감쇠고유주기 (실제 관측되는 주기)
c_Ns_per_m = 2.0 * zeta * np.sqrt(k_N_per_m * m_kg)   # 감쇠계수
c_cr_Ns_per_m = 2.0 * np.sqrt(k_N_per_m * m_kg)       # 임계감쇠계수

print("=" * 60)
print("SDOF 감쇠 자유진동")
print("=" * 60)
print(f"  질량      m  = {m_kg:.3e} kg")
print(f"  강성      k  = {k_N_per_m:.3e} N/m")
print(f"  감쇠비    z  = {zeta:.4f}")
print("-" * 60)
print(f"  고유각진동수 wn = {wn_rad_per_s:.4f} rad/s")
print(f"  고유주기     Tn = {Tn_s:.4f} s")
print(f"  감쇠고유주기 Td = {Td_s:.4f} s   (Tn 보다 {100*(Td_s/Tn_s-1):.3f}% 길다)")
print(f"  임계감쇠계수 ccr= {c_cr_Ns_per_m:.4e} N*s/m")
print(f"  감쇠계수     c  = {c_Ns_per_m:.4e} N*s/m")

# ---------------------------------------------------------------------------
# 4. 이론 해석해 (저감쇠)
#    x(t) = e^(-z*wn*t) * [ x0*cos(wd*t) + (v0 + z*wn*x0)/wd * sin(wd*t) ]
# ---------------------------------------------------------------------------
dt_s = Tn_s / pts_per_cycle
t_s = np.arange(0.0, n_cycles * Tn_s, dt_s)

A = x0_m
B = (v0_m_per_s + zeta * wn_rad_per_s * x0_m) / wd_rad_per_s
x_exact_m = np.exp(-zeta * wn_rad_per_s * t_s) * (
    A * np.cos(wd_rad_per_s * t_s) + B * np.sin(wd_rad_per_s * t_s)
)


# ---------------------------------------------------------------------------
# 5. 수치해 — Newmark-beta 평균가속도법 (gamma=1/2, beta=1/4, 무조건 안정)
#    Chopra, Dynamics of Structures, Table 5.4.2 의 표준 절차
# ---------------------------------------------------------------------------
def newmark_linear(m, c, k, p, dt, u0, v0, gamma=0.5, beta=0.25):
    """선형 SDOF의 Newmark 적분. p는 시간이력 하중 배열(자유진동이면 0 배열)."""
    n = len(p)
    u = np.zeros(n)
    v = np.zeros(n)
    a = np.zeros(n)

    u[0] = u0
    v[0] = v0
    a[0] = (p[0] - c * v0 - k * u0) / m          # 초기 가속도는 운동방정식에서 나온다

    k_hat = k + gamma / (beta * dt) * c + m / (beta * dt**2)
    a1 = m / (beta * dt**2) + gamma / (beta * dt) * c
    a2 = m / (beta * dt) + (gamma / beta - 1.0) * c
    a3 = (1.0 / (2.0 * beta) - 1.0) * m + dt * (gamma / (2.0 * beta) - 1.0) * c

    for i in range(n - 1):
        p_hat = p[i + 1] + a1 * u[i] + a2 * v[i] + a3 * a[i]
        u[i + 1] = p_hat / k_hat
        v[i + 1] = (
            gamma / (beta * dt) * (u[i + 1] - u[i])
            + (1.0 - gamma / beta) * v[i]
            + dt * (1.0 - gamma / (2.0 * beta)) * a[i]
        )
        a[i + 1] = (
            (u[i + 1] - u[i]) / (beta * dt**2)
            - v[i] / (beta * dt)
            - (1.0 / (2.0 * beta) - 1.0) * a[i]
        )
    return u, v, a


p_zero_N = np.zeros_like(t_s)                     # 자유진동 = 외력 0
x_num_m, _, _ = newmark_linear(
    m_kg, c_Ns_per_m, k_N_per_m, p_zero_N, dt_s, x0_m, v0_m_per_s
)

# ---------------------------------------------------------------------------
# 6. 검증 1 — 수치해 vs 이론해
# ---------------------------------------------------------------------------
err_max = np.max(np.abs(x_num_m - x_exact_m)) / np.max(np.abs(x_exact_m))
print("-" * 60)
print(f"[검증 1] Newmark vs 이론해 최대 상대오차 = {err_max*100:.4f} %")
print(f"         판정: {'[PASS]' if err_max < 1e-2 else '[FAIL] dt를 줄여라'}")

# ---------------------------------------------------------------------------
# 7. 검증 2 — 응답에서 감쇠비를 역산해 입력값을 복원한다 (대수감쇠율)
#    delta = (1/n) * ln( x_i / x_{i+n} ),   zeta = delta / sqrt(4*pi^2 + delta^2)
# ---------------------------------------------------------------------------
inner = x_exact_m[1:-1]
peak_idx = np.where((inner > x_exact_m[:-2]) & (inner > x_exact_m[2:]))[0] + 1
n_span = min(5, len(peak_idx) - 1)                 # 5주기 간격으로 계산 (정확도 향상)

delta = np.log(x_exact_m[peak_idx[0]] / x_exact_m[peak_idx[n_span]]) / n_span
zeta_back = delta / np.sqrt(4.0 * np.pi**2 + delta**2)
zeta_err = abs(zeta_back - zeta) / zeta

Td_measured_s = (t_s[peak_idx[n_span]] - t_s[peak_idx[0]]) / n_span

print("-" * 60)
print(f"[검증 2] 피크 {len(peak_idx)}개 검출, {n_span}주기 간격 사용")
print(f"         대수감쇠율      delta = {delta:.6f}")
print(f"         역산 감쇠비     zeta  = {zeta_back:.6f}  (입력 {zeta:.6f})")
print(f"         상대오차              = {zeta_err*100:.4f} %")
print(f"         측정 감쇠고유주기 Td  = {Td_measured_s:.4f} s  (이론 {Td_s:.4f} s)")
print(f"         판정: {'[PASS]' if zeta_err < 1e-2 else '[FAIL]'}")
print("=" * 60)

# ---------------------------------------------------------------------------
# 8. 그래프 — 축 라벨은 영문. 한글 폰트가 없는 PC에서 네모(tofu)로 깨지는 것을 피한다
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 4.5))

env = x0_m * np.exp(-zeta * wn_rad_per_s * t_s)   # 포락선 (감쇠의 시각적 증거)
ax.plot(t_s, env * 1e3, "--", color="0.6", lw=1.0, label=r"envelope $\pm x_0 e^{-\zeta\omega_n t}$")
ax.plot(t_s, -env * 1e3, "--", color="0.6", lw=1.0)
ax.plot(t_s, x_exact_m * 1e3, "-", lw=1.6, label="exact")
ax.plot(t_s[::10], x_num_m[::10] * 1e3, "o", ms=3.0, mfc="none", label=r"Newmark-$\beta$")
ax.plot(t_s[peak_idx], x_exact_m[peak_idx] * 1e3, "r.", ms=8, label="peaks (log-dec)")

ax.set_xlabel("Time  $t$  [s]")
ax.set_ylabel("Displacement  $x$  [mm]")
ax.set_title(
    f"SDOF free vibration   $T_n$={Tn_s:.3f} s, "
    rf"$\zeta$={zeta:.3f}  (back-calc {zeta_back:.4f})"
)
ax.grid(alpha=0.3)
ax.legend(loc="upper right", fontsize=9)
fig.tight_layout()

out_dir = Path(__file__).parent / "figs"          # 절대경로 금지 — 어느 PC에서든 동작
out_dir.mkdir(exist_ok=True)
out_png = out_dir / "sdof_free_response.png"
fig.savefig(out_png, dpi=150)
print(f"그래프 저장: {out_png}")

plt.show()
