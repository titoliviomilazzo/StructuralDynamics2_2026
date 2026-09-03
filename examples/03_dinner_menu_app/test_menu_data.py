import sys
import unittest
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(APP_DIR))

from menu_data import ASSETS_DIR, CUISINES, MENU_CATALOG  # noqa: E402


class MenuDataTests(unittest.TestCase):
    def test_expected_cuisine_order(self) -> None:
        self.assertEqual(CUISINES, ("한식", "중식", "양식", "일식"))

    def test_each_cuisine_has_multiple_choices(self) -> None:
        for cuisine in CUISINES:
            with self.subTest(cuisine=cuisine):
                self.assertGreaterEqual(len(MENU_CATALOG[cuisine]), 4)

    def test_image_mapping_points_to_local_assets(self) -> None:
        for cuisine, items in MENU_CATALOG.items():
            for item in items:
                with self.subTest(cuisine=cuisine, menu=item.name):
                    self.assertTrue(item.image_path.is_file(), item.image_path)
                    self.assertEqual(item.image_path.parent, ASSETS_DIR)

    def test_menu_names_are_unique_within_cuisine(self) -> None:
        for cuisine, items in MENU_CATALOG.items():
            with self.subTest(cuisine=cuisine):
                names = [item.name for item in items]
                self.assertEqual(len(names), len(set(names)))


if __name__ == "__main__":
    unittest.main()
