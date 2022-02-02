import os
import sys
import unittest
import logging

# Python sys path is created out of distribution packages, user packages installed with pip
# and PYTHONPATH environment variable. Inside those directories interpreter searches for modules to import.

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "site-packages"))


import pack

# DBG is global boolean variable
# Flags is static class with DEBUG flag
from pack import DBG, Flags

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s %(asctime)s [%(filename)13s:%(lineno)4d] %(message)s",
)

log = logging.getLogger()

DEBUG = True

def init():
    pass

class Tests(unittest.TestCase):
    def setUp(self):
        print()

    def test_global_nonmutable(self):
        global DBG
        log.debug(f"DBG address is {hex(id(DBG))}")
        log.debug(f"pack.DBG address is {hex(id(pack.DBG))}")
        self.assertEqual(DBG, True)
        log.info('Change imported "DBG" to False')
        DBG = False
        log.debug(f"DBG address is {hex(id(DBG))}")
        log.debug(f"pack.DBG address is {hex(id(pack.DBG))}")

        # When using non-mutable global objects, changing its value
        # changes its address as well, so if other modules uses it as
        # well theirs value won't be updated
        self.assertNotEqual(DBG, pack.DBG)

    def test_global_mutable(self):
        log.debug(f"Flags address is {hex(id(pack.Flags))}")
        log.debug(f"Flags.DEBUG address is {hex(id(pack.Flags.DEBUG))}")
        log.info(f'Set "Flags.DEBUG" to False')
        pack.clear_debug()
        log.debug(f"Flags address is {hex(id(pack.Flags))}")
        log.debug(f"Flags.DEBUG address is {hex(id(pack.Flags.DEBUG))}")

        # Flags class stores address of DEBUG and if DEBUG gets changes
        # address in Flags gets updated as well. So correct value of
        # DEBUG will be use in every module that import Flags
        self.assertEqual(Flags.DEBUG, pack.Flags.DEBUG)

    def test_local(self):
        Flags = {"DEBUG": True}

        # Global scope object redefinition, especially risky in large function
        # when we would like to use global variable, but it is redefined by local one
        # Once global variable gets redefined in functions, it cannot be accessed

        log.debug(f"{Flags=}")
        self.assertEqual(Flags["DEBUG"], True)


    def test_global(self):
        global DEBUG
        log.debug(f"DEBUG address is {hex(id(DEBUG))}")
        DEBUG = False
        log.debug(f"DEBUG address is {hex(id(DEBUG))}")
        self.assertTrue("DEBUG" in globals())
        self.assertFalse("DEBUG" in locals())


    def test_flag_in_class(self):
        log.debug(f"Flags address is {hex(id(Flags))}")
        log.debug(f"DEBUG address is {hex(id(Flags.DEBUG))}")
        Flags.DEBUG = True
        log.debug(f"DEBUG address is {hex(id(Flags.DEBUG))}")
        log.debug(f"Flags address is {hex(id(Flags))}")


    def test_local_override_global(self):
        DEBUG = False
        self.assertTrue("DEBUG" in globals())
        self.assertTrue("DEBUG" in locals())

    def test_global_function_local_variable(self):
        init = False
        with self.assertRaises(Exception):
            init()

    def test_example_part_1(self):
        """
        Define global variable, increment its value and check if it is propely incremented
        in test_example_part_2. Tests are executed in alphabetical order.
        """
        global variable
        variable = 0
        variable += 1
        # print(variable)

    def test_example_part_2(self):
        print(f"variable is now: {variable}")

if __name__ == "__main__":
    unittest.main(verbosity=2)
