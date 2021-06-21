from doctest import testmod
import unittest
import random


def randomnumbers():
    x = random.sample(range(1, 49), 6)
    print(x)
    return x


class RandomNums(unittest.TestCase):
    def setUp(self):
        self.a = 1
        self.b = 2

    def test_random_nums(self):
        randomnumbers()
        self.assertTrue(self.a >= 1 and self.b <= 49)
        if __name__ == "__main__":
            unittest.main()

    def testEnter(self):

