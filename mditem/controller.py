# from coins import Coins


class Item:
    DEFAULT_ITEM_LIST = [
        {
            "name": "Canned Coffee",
            "price": 120,
            "quantity": 2
        },
        {
            "name": "Water PET Bottle",
            "price": 100,
            "quantity": 0
        },
        {
            "name": "Sport Drinks",
            "price": 150,
            "quantity": 3
        },
        {
            "name": "Pepsi",
            "price": 150,
            "quantity": 33
        },
        {
            "name": "Coca Cola",
            "price": 120,
            "quantity": 22
        },
        {
            "name": "Slurpee",
            "price": 80,
            "quantity": 18
        },
    ]

    def __init__(self):
        self.ITEM_LIST = Item.DEFAULT_ITEM_LIST

    # cek item purchase
    def is_item_purchasable(self, item_idx, coin_amount, item_list):
        if item_idx > len(item_list):
            return False

        item_detail = item_list[item_idx]
        if item_detail["quantity"] == 0:
            return False

        item_price = item_detail["price"]

        if coin_amount >= item_price:

            return True

        # TODO, place at diff place
        print("Not enough coin")
        return False

    def item_deduction(self, outlet, item_list):
        for i in outlet:
            item_list[i["idx"]]["quantity"] -= 1
        return item_list
