import unittest
import unittest.mock as mock

from models.arithmetic import SimpleArithmeticProblem


class SimpleArithmeticProblemTest(unittest.TestCase):
    def setUp(self):
        pass

    @mock.patch('random.randint', return_value=2)
    def test_generate_digits(self):
        cls = SimpleArithmeticProblem(1)
        self.assertEqual(cls._generate_digit(1), 2)
