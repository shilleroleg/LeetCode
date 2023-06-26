
def _digit(number, operator):
    if operator is None:
        return number
    return operator(number)


def zero(operator=None): return _digit(0, operator)
def one(operator=None): return _digit(1, operator)
def two(operator=None): return _digit(2, operator)
def three(operator=None): return _digit(3, operator)
def four(operator=None): return _digit(4, operator)
def five(operator=None): return _digit(5, operator)
def six(operator=None): return _digit(6, operator)
def seven(operator=None): return _digit(7, operator)
def eight(operator=None): return _digit(8, operator)
def nine(operator=None): return _digit(9, operator)


def plus(second): return lambda first: first + second
def minus(second): return lambda first: first - second
def times(second): return lambda first: first * second
def divided_by(second): return lambda first: first / second


if __name__ == '__main__':
    print(one(plus(five())))         # 6
    print(seven(times(three())))     # 21
    print(nine(minus(six())))        # 3
    print(eight(divided_by(four()))) # 2
