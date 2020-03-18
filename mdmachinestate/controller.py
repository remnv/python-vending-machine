from mditem.controller import Item
from mdcoin.controller import Coin


class MachineState:
    def __init__(self):

        # users
        self.input_amount = 0
        self.change = {}
        self.return_gate = {}
        self.outlet = []

        self.provisional_coin = {}

        # vending
        item_obj = Item()
        coin_obj = Coin()
        self.vending_item = item_obj.ITEM_LIST
        self.vending_coin = coin_obj.COIN_LIST

    def reset(self):
        coin_obj = Coin()
        self.input_amount = 0
        self.change = []
        self.return_gate = []
        self.outlet = []

        self.provisional_coin = {i: 0 for i in coin_obj.VALID_COIN_LIST}

    def insert_coin(self, coin):
        coin_obj = Coin()
        if coin_obj.is_coin_usable(coin, self.vending_coin):
            self.provisional_coin[str(coin)] += 1
            self.input_amount += int(coin)

    def choose_item(self, index):
        item_obj = Item()
        if item_obj.is_item_purchasable(index, self.input_amount, self.vending_item):
            item_detail = self.vending_item[index]

            self.input_amount -= item_detail["price"]
            self.outlet.append({
                "idx": index,
                "name": item_detail["name"]
            })

    def get_item(self):
        item_obj = Item()
        self.vending_item = item_obj.item_deduction(
            self.outlet, self.vending_item)

    def pull_lever(self):
        coin_obj = Coin()
        self.return_gate = coin_obj.change_coin(
            self.input_amount, self.vending_coin)
        self.input_amount = 0

    def get_return_coin(self):
        self.reset()

    def _state(self):
        print("\n----------------------------------")
        print("[Input amount]\t\t", self.input_amount)
        print("[Change]\t\t", self.change)
        print("[Return gate]\t\t", self.return_gate)
        print("[Items for sale]\t", self.vending_item)
        print("[Outlet]\t\t", self.outlet)
        print("----------------------------------")
