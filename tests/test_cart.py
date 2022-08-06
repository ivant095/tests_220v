import unittest

#Наш объект тестирования
from cart import cart


class TestCart(unittest.TestCase):

    def test_1(self):

        result = cart([7, 3, 5, 9])

        self.assertEqual(
            [3, 5, 7, 9],
            result
        )

