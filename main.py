# from coins import Coins
# from items import Items
# from vendingmachine import VendingMachine
from mdmachinestate.controller import MachineState


if __name__ == '__main__':
    print("Starting..")
    # TODO, do data preparation here loading end

    close = False
    reset = False
    # vm_machine = VendingMachine()
    selected_item = None

    ms_obj = MachineState()
    ms_obj.reset()
    while close is False:
        if not reset:

            # state now
            ms_obj._state()

            # user input
            _cmd_raw = input("Machine command (close)?\n")

            # sanitizing space
            _cmd = list(filter(lambda x: x != "", _cmd_raw.split(" ")))
            if _cmd[0] == "1":
                coin_amount = int(_cmd[1])
                ms_obj.insert_coin(coin_amount)
                print("Insert coins")
                print("coin_amount:", coin_amount)

            elif _cmd[0] == "2":
                item = int(_cmd[1])
                ms_obj.choose_item(item-1)  # index 0
                print("Choose item to purchase")
                print("Chosen item:", item)

            elif _cmd[0] == "3":
                ms_obj.get_item()
                print("Get items")

            elif _cmd[0] == "4":
                ms_obj.pull_lever()
                print("Return coins")
                pass

            elif _cmd[0] == "5":
                ms_obj.get_return_coin()
                print("Get returned coins")

                reset = True
                pass

            else:
                close = True
        elif reset:
            ms_obj.reset()
            print("======================================")
            print("Ready again..")
            reset = False

        else:
            pass
