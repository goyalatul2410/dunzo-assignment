import unittest

from beverage_factory import main


class TestCoffeeMachine(unittest.TestCase):
    def test_outlets(self):
        self.assertEqual(main(["hot_tea", "hot_coffee", "black_tea", "green_tea"]), [True, True, False, False])
        self.assertEqual(main(["hot_tea", "black_tea", "hot_coffee", "green_tea"]), [True, False, True, False])
        self.assertEqual(main(["green_tea", "hot_tea", "hot_coffee", "black_tea"]), [False, True, True, False])
