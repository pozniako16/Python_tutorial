"""
Goal: Work on generator to create an iterator on the fibonacci suite
"""


def fib_generator():
    suite = 0
    first = 1
    for i in range(10):
        yield suite
        suite, first = suite + first, suite


def fib_printer():
    print("\n_________________GENERATORS_________________")
    for n in fib_generator():
        print(n)
