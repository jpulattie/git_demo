import random
import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):

    def test1(self):
        tests_to_generate = 490999

        for i in range(tests_to_generate):
            guider = random.randint(0, 9)
            if guider == 1:
                guided = self.num_builder2()
                credit_card_validator(guided)

            else:
                new_number = self.num_builder(random.randint(14, 17))
                credit_card_validator(new_number)

    def num_builder(self, length):
        number = ''
        for i in range(0, length):
            number = number + str(random.randint(0, 9))
        return number

    def num_builder2(self):
        number2 = str(random.randint(2220000000000000, 2800000000000000))
        return number2


if __name__ == '__main__':
    unittest.main()
