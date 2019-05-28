from unittest import TestCase

from scripts.ch02 import apply_discount


class TestChapter02(TestCase):

    def test_apply_discount(self):
        shoes = {'name': 'Fancy Shoes', 'price': 14900}
        assert apply_discount(shoes, 0.25) == 11175

    def test_apply_discount_fail(self):
        shoes = {'name': 'Fancy Shoes', 'price': 100}
        with self.assertRaises(AssertionError):
            apply_discount(shoes, -1)