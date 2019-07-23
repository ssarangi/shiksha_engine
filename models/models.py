from utils import string_formatting as sf
import exceptions


class BaseProblem:
    def __init__(self, complexity):
        self._complexity = complexity
        self._text_repr = None

    def generate(self):
        if self._text_repr is not None:
            return self._text_repr
        raise exceptions.ClassNotImplementedException()


class BaseSolution:
    pass


class Grade:
    def __init__(self, grade):
        self._grade = grade

    def get_grade(self):
        return self._grade
