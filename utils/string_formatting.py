def same_line(*args, delimiter=''):
    return delimiter.join([atr(arg) for arg in args])


def new_line():
    return '\n'
