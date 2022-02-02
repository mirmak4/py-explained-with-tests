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

    def test_fun_pos(self):
        def fun_pos(a, b):
            log.debug(f"{a=} {b=}")
            return a, b

        self.assertEqual(fun_pos(1, 2), (1, 2))
        self.assertEqual(fun_pos(1, b=2), (1, 2))
        self.assertEqual(fun_pos(a=1, b=2), (1, 2))
        self.assertEqual(fun_pos(b=2, a=1), (1, 2))
        with self.assertRaises(TypeError):
            fun_pos(1)

    def test_fun_key(self):
        def fun_key(a=1, b=2):
            log.debug(f"{a=} {b=}")
            return a, b

        self.assertEqual(fun_key(1, 2), (1, 2))
        self.assertEqual(fun_key(1, b=2), (1, 2))
        self.assertEqual(fun_key(a=1, b=2), (1, 2))
        self.assertEqual(fun_key(1), (1, 2))
        self.assertEqual(fun_key(a=1), (1, 2))
        self.assertEqual(fun_key(b=2), (1, 2))
        self.assertEqual(fun_key(b=2, a=1), (1, 2))
        with self.assertRaises(TypeError):
            fun_key(1, 2, 3)

    def test_fun_only_pos(self):
        def fun_only_pos(a, b, /):
            log.debug(f"{a=} {b=}")
            return a, b

        self.assertEqual(fun_only_pos(1, 2), (1, 2))
        with self.assertRaises(TypeError):
            fun_only_pos(1, b=2), (1, 2)

        with self.assertRaises(TypeError):
            fun_only_pos(a=1, b=2), (1, 2)

        with self.assertRaises(TypeError):
            fun_only_pos(b=2, a=1), (1, 2)


    def test_fun_only_key(self):
        def fun_only_key(*, a=1, b=2):
            log.debug(f"{a=} {b=}")
            return a, b

        self.assertEqual(fun_only_key(a=1, b=2), (1, 2))
        self.assertEqual(fun_only_key(a=1), (1, 2))
        self.assertEqual(fun_only_key(b=2), (1, 2))
        self.assertEqual(fun_only_key(b=2, a=1), (1, 2))
        with self.assertRaises(TypeError):
            fun_only_key(1, 2)

    def test_fun_mix(self):
        def fun_mix1(a=1, /, *, b=2):
            log.debug(f"{a=} {b=}")
            return a, b

        self.assertEqual(fun_mix1(1, b=2), (1, 2))
        self.assertEqual(fun_mix1(1), (1, 2))
        with self.assertRaises(TypeError):
            fun_mix1(a=1)


    def test_fun_args_list(self):
        def fun_args_list(a, /, *args, c=3):
            log.debug(f"{a=}, {args=}, {c=}")
            log.debug(f'"args" is a tuple - {isinstance(args, tuple)}')
            return a, *args, c

        # *args is equivalent to - args[0], args[1], ..., args[len(args)-1]

        self.assertEqual(fun_args_list(1), (1, 3))
        self.assertEqual(fun_args_list(1, 2), (1, 2, 3))
        self.assertEqual(fun_args_list(1, 2, c=3), (1, 2, 3))
        self.assertEqual(fun_args_list(*(1, 2), c=3), (1, 2, 3))
        with self.assertRaises(TypeError):
            fun_args_list(a=1, c=3), (1, 3)

    def test_fun_kwargs_dict(self):
        def fun_kwargs_dict(a, /, **kwargs):
            log.debug(f"{a=}, {kwargs=}")
            log.debug(f'"kwargs" is a dict - {isinstance(kwargs, dict)}')
            kwargs.setdefault("b", 4)
            return a, kwargs

        self.assertEqual(fun_kwargs_dict(1), (1, {"b": 4}))

        returned_dict = fun_kwargs_dict(1, b = 2, c = 3)[1]
        self.assertEqual(fun_kwargs_dict(2, **returned_dict), (2, {"b": 2, "c": 3}))

    def test_exercise(self):
        """
        Define function that takes 3 arguments:

            * first one can be only positional
            * second should be keyword argument but can be passed as positional as well
            * third shall be keyword argument and only can be passed as keyword arg.

        Function should display all passed arguments and return tuple with those - as in examples above.

        With function defined test possible calls with assertEqual.
        """

if __name__ == "__main__":
    unittest.main(verbosity=2)
