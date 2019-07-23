from collections import namedtuple
import random
import sympy

from models import BaseProblem
from log import logger


ArithmeticConfig = namedtuple(
    'ArithmeticConfig', ['num_digits', 'operators', 'total_sum'])


class SimpleArithmeticProblem(BaseProblem):
    """
    Class representing a simple arithmetic problem. These represent problems
    which represent combinations of simple arithmetic problems.
    """

    def __init__(self, complexity):
        super().__init__(complexity)
        self._complexity_mapping = {
            # For complexity 1, generate 1 digit numbers.
            1: ArithmeticConfig(1, '+,-', 10),
            # For complexity 2, generate 2 digit numbers.
            2: ArithmeticConfig(1, '+,-', 20),
            3: ArithmeticConfig(2, '+,-,*', 100),
            4: ArithmeticConfig(2, '+,-,*,/', 1000),
        }

    def _generate_digit(self, num_digits):
        return random.randint(pow(10, num_digits - 1), pow(10, num_digits) - 1)

    def _generate_two_operands_with_operator(self):
        config = self._complexity_mapping.get(
            self._complexity, ArithmeticConfig(2, '+,-,*,/', 1000))

        digit1 = self._generate_digit(config.num_digits)
        digit2 = self._generate_digit(config.num_digits)
        operator = random.choice(config.operators.split(','))
        # TODO(satyajit): Make sure to start using the total sum
        total_sum = config.total_sum
        str_repr = str(digit1) + operator + str(digit2)
        expr = sympy.sympify(str_repr, evaluate=False)
        self._text_repr = str_repr
        return expr

    def generate(self):
        return self._generate_two_operands_with_operator()
