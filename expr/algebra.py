"""
Generate algebraic expressions
"""
import random
import sympy

from . import operators

x, y, z = sympy.symbols('x y z')


def generate_single_symbol_expr(symbol, power: int, constant: int = None):
    if constant is None:
        constant = 1

    for i in range(0, power + 1):
        symbol = symbol * symbol
    return constant * symbol


def generate_single_symbol_multi_power_expr(symbol, max_power: int):
    expr = None
    for power in range(0, max_power + 1):
        curr_expr = generate_single_symbol_expr(
            symbol, power, random.randint(0, 10))
        print("Generated: %s" % curr_expr)
        if expr is None:
            expr = curr_expr
        else:
            random_operator = random.choice(operators.OPERATORS)
            print("Generated operator: %s" % random_operator)
            if random_operator == '+':
                expr += curr_expr
            elif random_operator == '-':
                expr -= curr_expr
            elif random_operator == '*':
                expr *= curr_expr
            elif random_operator == '/':
                expr /= curr_expr
    return expr

def generate_single_symbol_trigonometric_expr(symbol, trig_operators):
    trig_op = random.choice(trig_operators)
    return trig_op(symbol)
