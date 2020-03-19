

class Coin:
    DEFAULT_COIN_LIST = {
        "10": 21,
        "50": 5,
        "100": 3,
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

        # run out 10 coin
        if coin_list["10"] == 0:
            if coin > 10:
                return False

        elif coin == 10:
            return True

        # run out 100 coin
        elif coin_list["100"] == 0:
            if coin > 100:
                return False

        elif coin == 100:
            return True

        return True

    def is_change_possible(self, coin, coin_list):
        if coin_list["10"] < 9:
            return False

        if coin == 500 and coin_list["100"] < 4:
            return False

        return True

    def is_coin_check(self, coin, coin_list):
        if not self.is_valid_coin(coin):
            return False

        if not self.is_coin_usable(coin, coin_list):
            return False

        if not self.is_change_possible(coin, coin_list):
            return False

        return True

    def change_coin(self, coin_ammount, coin_list, last_gate):
        change_avl = [100, 10]
        change = last_gate

        for i in change_avl:
            count = int(coin_ammount / i)
            coin_ammount = coin_ammount-(i*count)

            data = {str(i): count}
            change = {**change, **data}

        return change

    def return_gate(self, coin, last_gate):
        coin = str(coin)

        result = {}
        if coin in last_gate:
            result = last_gate
            result[coin] = int(result[coin])+1
        else:
            result[coin] = 1
            result = {**result, **last_gate}

        return result
