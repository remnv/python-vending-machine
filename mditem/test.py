import unittest

from .controller import Item


class UnitTestItem(unittest.TestCase):

    def test_is_item_purchasable_true(self):
        item_obj = Item()
        item_list = [
            {
                "name": "Slurpee",
                "price": 80,
                "quantity": 18
            },
            {
                "name": "Coca Cola",
                "price": 120,
                "quantity": 22
            },
        ]
        item_chosen = 0
        coin_amount = 500

        expected = True
        self.assertEqual(expected, item_obj.is_item_purchasable(
            item_chosen, coin_amount, item_list))

    def test_is_item_purchasable_false(self):
        item_obj = Item()
        item_list = [
            {
                "name": "Slurpee",
                "price": 80,
                "quantity": 18
            },
            {
                "name": "Coca Cola",
                "price": 120,
                "quantity": 22
            },
        ]
        item_chosen = 0
        coin_amount = 10

        expected = False
        self.assertEqual(expected, item_obj.is_item_purchasable(
            item_chosen, coin_amount, item_list))

    def test_item_deduction(self):
        item_obj = Item()
        outlet = [
            {
                "idx": 0,
                "name": "Slurpee",
            },
            {
                "idx": 0,
                "name": "Slurpee",
            },
        ]
        item_list = [
            {
                "name": "Slurpee",
                "price": 80,
                "quantity": 18
            },
            {
                "name": "Coca Cola",
                "price": 120,
                "quantity": 22
            },
        ]

        expected = [
            {
                "name": "Slurpee",
                "price": 80,
                "quantity": 16
            },
            {
                "name": "Coca Cola",
                "price": 120,
                "quantity": 22
            },
        ]
        self.assertEqual(expected, item_obj.item_deduction(
            outlet, item_list))
