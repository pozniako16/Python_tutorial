"""
Goal: work on lambda expression
"""


def even_or_not():
    print("\n_________________LAMBDA_________________")
    l = [2, 4, 7, 3, 14, 19]
    print("Original list: " + l.__str__())
    for i in l:
        even_guesser = lambda n: (n % 2) == 0
        print(even_guesser(i))
