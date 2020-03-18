

class Coin:
    DEFAULT_COIN_LIST = {
        "10": 21,
        "50": 5,
        "100": 6,
        "500": 10,
    }

    def __init__(self):
        self.VALID_COIN_LIST = Coin.DEFAULT_COIN_LIST.keys()
        self.COIN_LIST = Coin.DEFAULT_COIN_LIST

    def is_valid_coin(self, coin):
        if str(coin) in self.VALID_COIN_LIST:
            return True

        return False

    def is_coin_usable(self, coin, coin_list):
        if not self.is_valid_coin(coin):
            return False

        if coin_list["10"] == 0:
            if coin > 10:
                return False

        elif coin == 10:
            return True

        elif coin_list["100"] == 0:
            if coin > 100:
                return False

        elif coin == 100:
            return True

        return True

    def change_coin(self, coin_ammount, coin_list):
        change_avl = [100, 10]
        change = {}

        for i in change_avl:
            count = int(coin_ammount / i)
            coin_ammount = coin_ammount-(i*count)

            data = {i: count}
            change = {**change, **data}

        return change

    # def is_change_possible(amount, all_coins_in_vending_machine):
    #     if all_coins_in_vending_machine["10"] < 9:
    #         return False
    #     if amount == 500 and all_coins_in_vending_machine["100"] < 4:
    #         return False
    #     if amount % 10 != 0:
    #         return False
    #     return True
