"""
예제 2 — 조화하중을 받는 SDOF의 정상응답과 공진
================================================

m*x'' + c*x' + k*x = p0*sin(w*t)

정상상태(steady-state) 해:
    x_p(t) = (p0/k) * Rd * sin(w*t - phi)
    Rd  = 1 / sqrt( (1-r^2)^2 + (2*z*r)^2 )      동적증폭계수
    phi = atan2( 2*z*r , 1-r^2 )                 위상각
    r   = w / wn                                 진동수비

이 스크립트가 보여주려는 것:

1. 동적증폭계수 곡선 — 공진(r≈1)에서 Rd_max ≈ 1/(2*z) 인 것을 수치로 확인
2. 과도응답이 사라진 뒤 수치해가 이론 정상해와 일치하는지 검증
3. 감쇠비가 공진 응답을 지배한다는 사실 (정적변위 대비 몇 배인가)

실행:  python harmonic_response.py
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# 1. 입력 — SI 기본단위 (kg, N, m, s)
# ---------------------------------------------------------------------------
m_kg = 1.0e5           # 100 ton
k_N_per_m = 4.0e6      # 4,000 kN/m
zeta = 0.05            # 감쇠비 5%

p0_N = 5.0e4           # 조화하중 진폭 50 kN
r_check = 1.0          # 시간이력으로 검증할 진동수비 (1.0 = 공진)

n_force_cycles = 60    # 하중 몇 주기까지 계산할 것인가 (과도응답이 사라질 만큼)
pts_per_cycle = 400

# ---------------------------------------------------------------------------
# 2. 단위 방어선
# ---------------------------------------------------------------------------
assert 1e3 < m_kg < 1e8, f"m_kg={m_kg}: kg가 맞는가 (ton 그대로 넣지 않았는가)"
assert 1e5 < k_N_per_m < 1e10, f"k_N_per_m={k_N_per_m}: N/m가 맞는가 (kN/m 그대로 넣지 않았는가)"
assert 0.0 < zeta < 1.0, f"zeta={zeta}: 5%는 0.05다"
assert 1e2 < p0_N < 1e9, f"p0_N={p0_N}: N이 맞는가 (kN 그대로 넣지 않았는가)"

# ---------------------------------------------------------------------------
# 3. 동특성과 정적 기준값
# ---------------------------------------------------------------------------
wn_rad_per_s = np.sqrt(k_N_per_m / m_kg)
Tn_s = 2.0 * np.pi / wn_rad_per_s
c_Ns_per_m = 2.0 * zeta * np.sqrt(k_N_per_m * m_kg)
x_static_m = p0_N / k_N_per_m          # 같은 크기 하중을 정적으로 걸었을 때의 변위

print("=" * 62)
print("SDOF 조화하중 정상응답")
print("=" * 62)
print(f"  Tn = {Tn_s:.4f} s,  wn = {wn_rad_per_s:.4f} rad/s,  zeta = {zeta:.3f}")
print(f"  정적변위 x_st = p0/k = {x_static_m*1e3:.4f} mm")


def Rd(r, z):
    """동적증폭계수."""
    return 1.0 / np.sqrt((1.0 - r**2) ** 2 + (2.0 * z * r) ** 2)


def phase_rad(r, z):
    """위상각 (하중 대비 응답이 뒤처지는 각). 0~pi."""
    return np.arctan2(2.0 * z * r, 1.0 - r**2)


# ---------------------------------------------------------------------------
# 4. 검증 1 — 공진 근사식 Rd_max ≈ 1/(2*zeta)
#    정확한 최대는 r = sqrt(1-2*z^2) 에서 발생하고 Rd = 1/(2*z*sqrt(1-z^2)) 이다.
# ---------------------------------------------------------------------------
r_peak_exact = np.sqrt(1.0 - 2.0 * zeta**2)
Rd_peak_exact = 1.0 / (2.0 * zeta * np.sqrt(1.0 - zeta**2))
Rd_approx = 1.0 / (2.0 * zeta)

r_grid = np.linspace(0.0, 3.0, 3001)
Rd_grid = Rd(r_grid, zeta)
r_peak_num = r_grid[np.argmax(Rd_grid)]
Rd_peak_num = Rd_grid.max()

print("-" * 62)
print("[검증 1] 공진 피크")
print(f"  수치 탐색   r = {r_peak_num:.4f},  Rd = {Rd_peak_num:.4f}")
print(f"  이론 정확값 r = {r_peak_exact:.4f},  Rd = {Rd_peak_exact:.4f}")
print(f"  간이 근사식 1/(2*zeta)      = {Rd_approx:.4f}")
ok1 = abs(Rd_peak_num - Rd_peak_exact) / Rd_peak_exact < 1e-3
print(f"  판정: {'[PASS]' if ok1 else '[FAIL]'}")


# ---------------------------------------------------------------------------
# 5. 시간이력 — Newmark-beta (예제 1과 동일한 함수. 초심자용으로 일부러 복사해 둠)
# ---------------------------------------------------------------------------
def newmark_linear(m, c, k, p, dt, u0, v0, gamma=0.5, beta=0.25):
    n = len(p)
    u = np.zeros(n)
    v = np.zeros(n)
    a = np.zeros(n)
    u[0], v[0] = u0, v0
    a[0] = (p[0] - c * v0 - k * u0) / m

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


w_rad_per_s = r_check * wn_rad_per_s
T_force_s = 2.0 * np.pi / w_rad_per_s
dt_s = T_force_s / pts_per_cycle
t_s = np.arange(0.0, n_force_cycles * T_force_s, dt_s)

p_N = p0_N * np.sin(w_rad_per_s * t_s)
x_num_m, _, _ = newmark_linear(m_kg, c_Ns_per_m, k_N_per_m, p_N, dt_s, 0.0, 0.0)

# 이론 정상해 (과도항 제외)
Rd_check = Rd(r_check, zeta)
phi_check = phase_rad(r_check, zeta)
x_ss_m = x_static_m * Rd_check * np.sin(w_rad_per_s * t_s - phi_check)

# ---------------------------------------------------------------------------
# 6. 검증 2 — 마지막 5주기에서 수치해가 이론 정상해로 수렴했는가
#    (앞부분은 과도응답이 살아 있으므로 비교 대상이 아니다)
# ---------------------------------------------------------------------------
tail = slice(-5 * pts_per_cycle, None)
amp_num_m = np.max(np.abs(x_num_m[tail]))
amp_ss_m = x_static_m * Rd_check
amp_err = abs(amp_num_m - amp_ss_m) / amp_ss_m
wave_err = np.max(np.abs(x_num_m[tail] - x_ss_m[tail])) / amp_ss_m

print("-" * 62)
print(f"[검증 2] r = {r_check:.2f} 시간이력 (하중 {n_force_cycles}주기)")
print(f"  이론 Rd            = {Rd_check:.4f}")
print(f"  이론 정상 진폭     = {amp_ss_m*1e3:.4f} mm  (= x_st x Rd)")
print(f"  수치 마지막 5주기  = {amp_num_m*1e3:.4f} mm")
print(f"  진폭 상대오차      = {amp_err*100:.4f} %")
print(f"  파형 최대 상대오차 = {wave_err*100:.4f} %")
print(f"  위상 지연 phi      = {np.degrees(phi_check):.2f} deg")
ok2 = amp_err < 1e-2 and wave_err < 2e-2
print(f"  판정: {'[PASS]' if ok2 else '[FAIL] 주기 수 또는 dt를 조정하라'}")

print("-" * 62)
print("[해석] 정적 대비 증폭")
for z in (0.02, 0.05, 0.10, 0.20):
    print(f"  zeta={z:4.2f} -> 공진 시 최대 {1.0/(2*z*np.sqrt(1-z**2)):6.2f} 배")
print("  감쇠비를 5% -> 10%로 올리면 공진 응답이 약 절반이 된다.")
print("  제진(damper) 설계가 감쇠비를 목표로 삼는 이유가 여기 있다.")
print("=" * 62)

# ---------------------------------------------------------------------------
# 7. 그래프 (축 라벨 영문 — 한글 폰트 없는 PC에서 깨지지 않게)
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(15, 4.2))

# (a) 동적증폭계수
ax = axes[0]
for z in (0.02, 0.05, 0.10, 0.20):
    ax.plot(r_grid, Rd(r_grid, z), lw=1.5, label=rf"$\zeta$={z:.2f}")
ax.axvline(1.0, color="0.7", ls=":", lw=1.0)
ax.set_xlabel(r"Frequency ratio  $r=\omega/\omega_n$")
ax.set_ylabel(r"$R_d = x_0 / x_{st}$")
ax.set_title("Dynamic magnification")
ax.set_ylim(0, 26)
ax.grid(alpha=0.3)
ax.legend(fontsize=9)

# (b) 위상각
ax = axes[1]
for z in (0.02, 0.05, 0.10, 0.20):
    ax.plot(r_grid, np.degrees(phase_rad(r_grid, z)), lw=1.5, label=rf"$\zeta$={z:.2f}")
ax.axvline(1.0, color="0.7", ls=":", lw=1.0)
ax.axhline(90.0, color="0.7", ls=":", lw=1.0)
ax.set_xlabel(r"Frequency ratio  $r$")
ax.set_ylabel(r"Phase lag  $\phi$  [deg]")
ax.set_title(r"Phase angle ($\phi=90^\circ$ at resonance)")
ax.grid(alpha=0.3)

# (c) 시간이력
ax = axes[2]
ax.plot(t_s / Tn_s, x_num_m * 1e3, lw=1.2, label=r"Newmark-$\beta$ (total)")
ax.plot(t_s / Tn_s, x_ss_m * 1e3, "--", lw=1.0, color="C3", label="steady-state (theory)")
ax.axhline(x_static_m * 1e3, color="0.5", ls=":", lw=1.0, label=r"$x_{st}$")
ax.set_xlabel(r"Time  $t/T_n$")
ax.set_ylabel("Displacement  [mm]")
ax.set_title(f"Time history at $r$={r_check:.2f}")
ax.grid(alpha=0.3)
ax.legend(fontsize=8, loc="lower right")

fig.tight_layout()

out_dir = Path(__file__).parent / "figs"
out_dir.mkdir(exist_ok=True)
out_png = out_dir / "harmonic_response.png"
fig.savefig(out_png, dpi=150)
print(f"그래프 저장: {out_png}")

plt.show()
