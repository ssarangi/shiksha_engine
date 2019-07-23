"""
Generate simple numberic expressions
"""
import random


def generate_digits(num_digits: int) -> int:
    return random.randint(pow(10, num_digits - 1), pow(10, num_digits) - 1)
