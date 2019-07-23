from collections import namedtuple
import random
import sympy

from models import BaseProblem
from log import logger

# allowed_expr: expressions like cos, sin, tan, log, exp etc
# allowed_subexpr: expressions like x^2(power), 2 * x (constant *), 2 / x,
AlgebraicConfig = namedtuple('AlgebraicConfig', ['allowed_expr', 'allowed_subexpr'])

class SimpleAlgebraicProblem(BaseProblem):
    """
    Class representing a simple algebraic problem. These represent problems
    which represent combinations of simple algebraic problems.
    """

    def __init__(self, complexity):
        super().__init__(complexity)
        self._complexity_mapping = {
            # For complexity 1, generate simple expression
            1: AlgebraicConfig()
        }