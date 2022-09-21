"""
Goal: Work on list comprehension to simplify data processing
"""


def keep_only_positive():
    print("\n_________________LIST COMPREHENSION_________________")
    numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    positives = [positive for positive in numbers if positive >= 0]
    print("Original: " + numbers.__str__())
    print("Only +: " + positives.__str__())
