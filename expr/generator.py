"""
generator.py: This is the main file which should be used by other api's to generate
various math expressions. Other files in this directory are not meant to be exported.
"""

from . import algebra


def generate_single_symbol_expr():
    return algebra.generate_single_symbol_multi_power_expr(algebra.x, 2)
