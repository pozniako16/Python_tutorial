"""
Goal: define functions that can take various number of arguments
"""


def foo(a, b, c, *other):
    print(len(other))


def bar(a, b, c, **other):
    if other.get("magic_number") == 7:
        print(True)
    else:
        print(False)


def foo_bar():
    print("\n_________________VARIABLE NBR ARGS_________________")
    foo(1, 2, 3, 4, 5, 6, 7)
    bar(1, 2, 3, magic_number=7)
    bar(1, 2, 3, magic_number=1)