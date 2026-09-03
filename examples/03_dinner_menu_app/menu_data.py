from dataclasses import dataclass
from pathlib import Path
from typing import Final


@dataclass(frozen=True)
class MenuItem:
    name: str
    subtitle: str
    image_name: str

    @property
    def image_path(self) -> Path:
        return ASSETS_DIR / self.image_name


APP_DIR: Final[Path] = Path(__file__).resolve().parent
ASSETS_DIR: Final[Path] = APP_DIR / "assets"
CUISINES: Final[tuple[str, ...]] = ("한식", "중식", "양식", "일식")

MENU_CATALOG: Final[dict[str, tuple[MenuItem, ...]]] = {
    "한식": (
        MenuItem("비빔밥", "고소한 참기름 향과 다채로운 나물이 어우러진 든든한 한 그릇", "cooked_rice.svg"),
        MenuItem("김치찌개", "칼칼한 국물에 돼지고기와 김치가 진하게 배어든 집밥 메뉴", "pot_of_food.svg"),
        MenuItem("불고기", "달콤짭짤하게 구운 소고기로 누구나 편하게 즐기기 좋은 메뉴", "meat_on_bone.svg"),
        MenuItem("삼겹살", "노릇하게 구워 쌈채소와 곁들이기 좋은 저녁 단골 메뉴", "cooked_rice.svg"),
    ),
    "중식": (
        MenuItem("짜장면", "춘장 소스의 진한 감칠맛이 살아 있는 클래식 중화요리", "steaming_bowl.svg"),
        MenuItem("짬뽕", "해산물과 채소를 얼큰하게 끓여낸 뜨끈한 면 요리", "steaming_bowl.svg"),
        MenuItem("탕수육", "바삭한 튀김과 새콤달콤 소스의 조합이 매력적인 인기 메뉴", "takeout_box.svg"),
        MenuItem("마파두부", "화자오 향과 매콤한 두반장 소스가 돋보이는 밥도둑 메뉴", "takeout_box.svg"),
    ),
    "양식": (
        MenuItem("토마토 파스타", "산뜻한 토마토 소스와 면의 조화가 부담 없는 저녁 메뉴", "spaghetti.svg"),
        MenuItem("스테이크", "육즙 가득한 메인 요리로 특별한 저녁 분위기를 내기 좋은 선택", "meat_on_bone.svg"),
        MenuItem("리소토", "크리미한 식감과 진한 풍미가 매력적인 이탈리안 라이스 메뉴", "curry_rice.svg"),
        MenuItem("페퍼로니 피자", "짭짤한 토핑과 치즈가 어우러져 만족도가 높은 메뉴", "pizza.svg"),
    ),
    "일식": (
        MenuItem("초밥", "신선한 재료와 밥의 균형이 매력적인 깔끔한 메뉴", "sushi.svg"),
        MenuItem("라멘", "진한 육수와 쫄깃한 면발로 속까지 따뜻해지는 한 그릇", "steaming_bowl.svg"),
        MenuItem("가츠동", "바삭한 돈가스와 달큰한 소스가 밥과 잘 어울리는 덮밥", "bento_box.svg"),
        MenuItem("오야코동", "부드러운 달걀과 닭고기를 포근하게 얹은 일본식 덮밥", "bento_box.svg"),
    ),
}
