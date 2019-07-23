import random
from log import logger

from models.arithmetic import SimpleArithmeticProblem

from expr import generator

def generate_problem(cls):
    for i in range(1, 10):
        complexity = random.randint(1, 4)
        problem = cls(complexity)
        logger.info('Complexity: %s --> %s', complexity, problem.generate())

def generate_simple_arithmetic_problem():
    generate_problem(SimpleArithmeticProblem)

def generate_simple_algebraic_expression_problem():
    generate_problem()

def main():
    generate_simple_arithmetic_problem()
    expr = generator.generate_single_symbol_expr()
    print(expr)


if __name__ == "__main__":
    main()
