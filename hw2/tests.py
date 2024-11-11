import unittest
from contrived_func import contrived_func


class TestFunc(unittest.TestCase):

    def test_0(self):
        "test for all trues"
        val = 0
        self.assertTrue(contrived_func(val))

    def test_neg1(self):
        "test for all trues"
        val = -1
        self.assertTrue(contrived_func(val))

    def test_neg2(self):
        "test for all trues"
        val = -2
        self.assertTrue(contrived_func(val))

    def test_22(self):
        "test for all trues"
        val = 22
        self.assertTrue(contrived_func(val))

    def test_23(self):
        "test for all trues"
        val = 23
        self.assertTrue(contrived_func(val))

    def test_18(self):
        "test for all trues"
        val = 18
        self.assertTrue(contrived_func(val))

    def test_15(self):
        "test for all trues"
        val = 15
        self.assertTrue(contrived_func(val))

    def test_19(self):
        "test for all trues"
        val = 19
        self.assertTrue(contrived_func(val))


if __name__ == '__main__':
    unittest.main()
