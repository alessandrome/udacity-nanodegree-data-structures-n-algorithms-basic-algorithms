def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return None
    min_int = max_int = ints[0]
    for integer in ints:
        if integer > max_int:
            max_int = integer
        elif integer < min_int:
            min_int = integer
    return min_int, max_int


# Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if ((-10, 60) == get_min_max([1, 2, 4, 6, -3, 34, 23, 11, 10, 36, 60, -10])) else "Fail")
print("Pass" if ((5, 5) == get_min_max([5])) else "Fail")
print("Pass" if ((-10, 60) == get_min_max([1, 2, 4, 6, -3, 34, 23, 11, 10, 36, 60, -10])) else "Fail")
