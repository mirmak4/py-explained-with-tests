import logging
import unittest
import sys
import os
import time
import functools
import random

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s %(asctime)s [%(filename)13s:%(lineno)4d] %(message)s",
)

log = logging.getLogger()

# decorators are wrappers that can be applied on functions and class __call__ methods
# decorators can by applied with @ sign and name of function that implements decorator

class Tests(unittest.TestCase):
    def setUp(self):
        print()

    def test_simplest_decorator(self):

        def simplest_decorator(fun):
            log.debug("Decorate function")
            return fun

        @simplest_decorator
        def simple_function():
            log.debug("Simple function")
            return True

        self.assertTrue(simple_function())
        self.assertTrue(simple_function())

    def test_decorator_wit_closure(self):

        def decorator_with_closure(fun):
            def wrapper(*args, **kwargs):
                log.debug("Decorated function")
                return fun(*args, **kwargs)
            return wrapper

        @decorator_with_closure
        def simple_function():
            log.debug("Simple function")
            return True

        self.assertTrue(simple_function())
        self.assertTrue(simple_function())

    def test_decorator_to_upper(self):

        def to_upper(fun):
            def wrapper(*args, **kwargs):
                result : str = fun(*args, **kwargs)
                return result.upper()
            return wrapper

        def get_string():
            return "python"

        self.assertEqual(get_string(), "python")
        self.assertEqual(to_upper(get_string)(), "PYTHON")

    def test_parametrized_decorator(self):

        def repeat(num : int = 4):
            def _decor(fun):
                @functools.wraps(fun)
                def _wrapper(*args, **kwargs):
                    results = []
                    for _ in range(num):
                        results.append(fun(*args, **kwargs))
                    return results
                return _wrapper
            return _decor

        @repeat(20)
        def get_time():
            time_now = time.time()
            log.debug(f"Float timestamp is {time_now}")
            return time.time()

        results = get_time()

        self.assertEqual(get_time.__name__, "get_time")
        # self.assertGreater(results.pop(), results.pop())
        results = get_time()
        res1 = results.pop()
        for x in range(15):
            results.pop()
        res2 = results.pop()
        self.assertGreater(res1, res2)

        randoms = repeat(2)(random.random)()
        self.assertNotEqual(randoms.pop(), randoms.pop())

    def test_exercise(self):
        """Define retry decorator, that runs
        decorated function until successfull (result evaluated to True)
        or until maximum number of retries has been reached"""

        def retry(num = 5):
            print('retry')
            def _decor(fun):
                print('decor')
                @functools.wraps(fun)
                def _wrapper(*args, **kwargs):
                    # write your part here
                    result = None
                    for _ in range(num):
                        result = fun(*args, **kwargs)
                        if bool(result):
                            return result
                    else:
                        return result
                    # print('wrapper')
                    # try:
                    #     i = 0
                    #     results_gen = args[0]
                    #     while i < num-1:
                    #         result = next(results_gen)
                    #         if result:
                    #             return True
                    #         i += 1
                    #     return fun(*args, **kwargs)
                    # except StopIteration:
                    #     return False
                    # return fun(*args, **kwargs)
                return _wrapper
            return _decor

        results = (result for result in [False, False, True, False, True])
        results2 = (result for result in [False, False, False, False, False])
        results3 = (result for result in [False, False, False, False, False, True])
        results4 = (result for result in [False, False, False, False, True])
        results5 = (result for result in [False, False, False])

        @retry()
        def retried_function(params):
            try:
                # print("try")
                # log.debug("asdadf")
                return next(params)
            except StopIteration:
                return False

        # retried_function(results)
        # retry()(retried_function)(results)
        self.assertTrue(retried_function(results))
        self.assertFalse(retried_function(results2))
        self.assertFalse(retried_function(results3))
        self.assertTrue(retried_function(results4))
        self.assertFalse(retried_function(results5))
 
if __name__ == "__main__":
    unittest.main(verbosity=2)
