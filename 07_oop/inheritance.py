import logging
import unittest
from abc import ABC, abstractmethod

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s %(asctime)s [%(filename)13s:%(lineno)4d] %(message)s",
)

log = logging.getLogger()


class Shape(ABC):
    @abstractmethod
    def get_surface_area(self):
        ...


class Rectangle(Shape):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def get_surface_area(self):
        return self.side_a * self.side_b


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Triangle(Shape):
    def __init__(self, hight, bottom_side):
        self.hight = hight
        self.bottom_side = bottom_side


class Tests(unittest.TestCase):
    def setUp(self):
        print()

    def test_cant_create_abstract_base(self):
        with self.assertRaises(TypeError):
            shape = Shape()

    def test_shape_without_surface_method(self):
        with self.assertRaises(TypeError):
            triangle = Triangle(3,5)

    def test_square_rectangle_area(self):
        rectangle = Rectangle(3, 3)
        square = Square(3)

        self.assertEqual(rectangle.get_surface_area(), rectangle.get_surface_area())


if __name__ == "__main__":
    unittest.main(verbosity=2)
