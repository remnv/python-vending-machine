import unittest
# import sys

from mdcoin.test import UnitTestCoin
from mditem.test import UnitTestItem
from mdmachinestate.test import UnitTestMachineState


class UnitTesting(UnitTestCoin,
                  UnitTestItem,
                  UnitTestMachineState):

    pass


if __name__ == '__main__':
    unittest.main()
    # module = sys.argv[0]
