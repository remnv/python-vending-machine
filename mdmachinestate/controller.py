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

        # TODO changeable or no mode
        self.change = {
            "100": 0,
            "10": 30,
        }

        self.input_amount = 0
        self.return_gate = []
        self.outlet = []

        self.provisional_coin = {str(i): 0 for i in coin_obj.VALID_COIN_LIST}

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
        # self.reset()
        pass

    def _state(self):
        print("\n==================================")

        # tab space
        tbs = 25

        title = "[Input amount]"
        print(title, "-"*(tbs-len(title)))
        print(" "*tbs, "%s JPY" % (self.input_amount))

        title = "[Change]"
        print(title, "-"*(tbs-len(title)))
        ch = self.change
        for i in ch:
            print(" "*tbs, "%s JPY" % (i), " "*(13-len(str(i))), "%s" %
                  ("Change" if ch[i] != 0 else "No Change"))

        title = "[Return gate]"
        print(title, "-"*(tbs-len(title)))
        rg = self.return_gate
        if rg:
            for i in rg:
                text = "%s%s\n" % (" "*tbs, "%s JPY" % i)
                text = text*rg[i]
                print(text[:-2])
        else:
            print(" "*tbs, "Empty")

        title = "[Items for sale]"
        print(title, "-"*(tbs-len(title)))
        no = 1
        for i in self.vending_item:
            print(" "*tbs, "%s. %s" % (no, i["name"]),
                  " "*(20-len(i["name"])), "%s JPY" % (i["price"]),
                  " "*(7-len(str(i["price"]))), "%s" % (i["quantity"]))
            no += 1

        title = "[Outlet]"
        print(title, "-"*(tbs-len(title)))
        if self.outlet:
            for i in self.outlet:
                print(" "*tbs, "%s" % (i["name"]))
        else:
            print(" "*tbs, "Empty")

        print("\n==================================")
