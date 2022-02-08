import logging
import unittest
from typing import Union

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s %(asctime)s [%(filename)13s:%(lineno)4d] %(message)s",
)

log = logging.getLogger()


class MyNum:
    def __init__(self, x: Union[float, int]):
        self.x = x

    def __lt__(self, y):
        return self.x < float(y)

    def __eq__(self, y):
        return float(self) == float(y)

    def __int__(self):
        return int(self.x)

    def __float__(self):
        return float(self.x)

    def __str__(self):
        return f"{self.x}"

    def __repr__(self):
        return str(self)


class MyList:
    def __init__(self, vals):
        self.vals = vals

    def __len__(self):
        return len(self.vals)

    def __getitem__(self, key):
        return self.vals[key]

    def __setitem__(self, key, value):
        self.vals[key] = value

    def __delitem__(self, key):
        del self.vals[key]

    def __iter__(self):
        return iter(self.vals)

    def __repr__(self):
        return str(self.vals)

    def sort(self):
        return self.vals.sort()


class Tests(unittest.TestCase):
    def setUp(self):
        print()

    def test_my_types(self):

        list_a = MyList([MyNum(1), MyNum(4), MyNum(2), MyNum(5.0), MyNum(-2), MyNum(5), MyNum(1)])

        self.assertEqual(min(list_a), -2)
        self.assertEqual(max(list_a), 5)

        list_b = sorted(list_a)
        list_a.sort()

        # TODO try to fix it
        # self.assertEqual(list_a, list_b)

        for ele_a, ele_b in zip(list_a, list_b):
            self.assertEqual(ele_a, ele_b)


if __name__ == "__main__":
    unittest.main(verbosity=2)
