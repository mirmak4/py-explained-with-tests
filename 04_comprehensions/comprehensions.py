import logging
import unittest

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s %(asctime)s [%(filename)13s:%(lineno)4d] %(message)s",
)

log = logging.getLogger()


class Tests(unittest.TestCase):
    def setUp(self):
        print()

    def test_list_with_one_loop(self):
        def list_with_one_loop():
            lst = []
            for i in range(5):
                lst.append(i * 2)
            return lst

        list_comprehension = [i * 2 for i in range(5)]
        log.debug(f"{list_comprehension=}")
        self.assertEqual(list_with_one_loop(), list_comprehension)

    def test_list_with_two_loops(self):
        def list_with_two_loops():
            rows = []
            for i in range(11):
                col = []
                for j in range(11):
                    col.append(i * j)
                rows.append(col)
            return rows

        list_comprehension = [[i * j for i in range(11)] for j in range(11)]
        self.assertEqual(list_with_two_loops(), list_comprehension)

    def test_set_example(self):
        def set_example():
            modulo_7 = set()
            for i in range(4, 29, 2):
                modulo_7.add(i % 7)
            return modulo_7

        set_comprehension = {i % 7 for i in range(4, 29, 2)}
        log.debug(f"{set_comprehension=}")
        self.assertEqual(set_example(), set_comprehension)

    def test_dict_example(self):
        def dict_example():
            modulo_7 = {}
            for i in range(4, 9, 2):
                modulo_7[i] = i % 7
            return modulo_7
        dict_comprehension = {i: i % 7 for i in range(4, 9, 2)}

        log.debug(f"{dict_comprehension=}")
        self.assertEqual(dict_example(), dict_comprehension)

    def test_set_with_filter(self):
        words = {"abc", "", "b", "ADB", "car", "home"}

        def set_with_filter():
            filtered_words = set()
            for word in words:
                if len(word) > 2:
                    filtered_words.add(word)
            return filtered_words

        set_comprehension = {word for word in words if len(word) > 2}
        log.debug(f"{set_comprehension=}")
        self.assertEqual(set_with_filter(), set_comprehension)

    def test_exercise(self):
        """
        Define closure and similar comprehension.

        Both should create new list of words without words that start with underscore.
        """
        words = ("__init__", "__call__", "configure", "start", "stop")
        def set_with_filter():
            filtered_words = set()
            for word in words:
                if not word.startswith('_'):
                    filtered_words.add(word)
            return filtered_words
        # print( set_with_filter() )
        set_comprehension = {w for w in words if not w.startswith('_')}
        lambda_comp = filter(lambda w: not w.startswith('_'), words)
        set_lambda_comp = set(lambda_comp)
        log.debug(f"{set_comprehension=}")
        self.assertEqual(set_with_filter(), set_comprehension)
        self.assertEqual(set_with_filter(), set_lambda_comp)
        self.assertTrue("__init__" not in set_with_filter())
        self.assertTrue("__call__" not in set_with_filter())
        self.assertTrue("__init__" not in set_comprehension)
        self.assertTrue("__call__" not in set_comprehension)
        self.assertTrue("__init__" not in set_lambda_comp)
        self.assertTrue("__call__" not in set_lambda_comp)

if __name__ == "__main__":
    unittest.main(verbosity=2)
