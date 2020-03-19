import unittest

from .controller import Coin


class UnitTestCoin(unittest.TestCase):

    def test_is_valid_coin_true(self):
        coin_obj = Coin()
        inserted_coin = 500

        expected = True
        self.assertEqual(expected, coin_obj.is_valid_coin(inserted_coin))

    def test_is_valid_coin_false(self):
        coin_obj = Coin()
        inserted_coin = 20

        expected = False
        self.assertEqual(expected, coin_obj.is_valid_coin(inserted_coin))

    def test_is_coin_usable_true(self):
        coin_obj = Coin()
        coin_list = {"10": 3, "100": 2}
        inserted_coin = 50

        expected = True
        self.assertEqual(expected, coin_obj.is_coin_usable(
            inserted_coin, coin_list))

    def test_is_coin_usable_false(self):
        coin_obj = Coin()
        coin_list = {"10": 0, "100": 2}
        inserted_coin = 50

        expected = False
        self.assertEqual(expected, coin_obj.is_coin_usable(
            inserted_coin, coin_list))

    def test_change_coin_is_check_true(self):
        coin_obj = Coin()
        last_gate = {}
        coin_list = {
            "10": 21,
            "50": 5,
            "100": 6,
            "500": 10,
        }
        leftover_coin = 380

        expected = {
            "100": 3,
            "10": 8
        }
        self.assertEqual(expected,
                         coin_obj.change_coin(leftover_coin, coin_list, last_gate))

    def test_change_coin_is_check_true(self):
        coin_obj = Coin()
        last_gate = {
            "500": 3
        }
        coin_list = {
            "10": 21,
            "50": 5,
            "100": 6,
            "500": 10,
        }
        leftover_coin = 380

        expected = {
            "100": 3,
            "10": 8,
            "500": 3,
        }
        self.assertEqual(expected,
                         coin_obj.change_coin(leftover_coin, coin_list, last_gate))

    def test_return_gate_empty_gate(self):
        coin_obj = Coin()
        last_gate = {}
        inserted_coin = 500

        expected = {
            "500": 1,
        }
        self.assertEqual(expected,
                         coin_obj.return_gate(inserted_coin, last_gate))

    def test_return_gate_fill_gate(self):
        coin_obj = Coin()
        last_gate = {
            "500": 3
        }
        inserted_coin = 40

        expected = {
            "500": 3,
            "40": 1,
        }
        self.assertEqual(expected,
                         coin_obj.return_gate(inserted_coin, last_gate))
