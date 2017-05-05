"""
A utility for generating test files.
"""
import random

from optimal_fingerings import N2F


ALL_NUMS = list(N2F.keys())


def single_test(size):
    """
    Creates a single test file of specified length.
    """
    with open(f'test_files/test_{size}.txt', 'w') as file:
        file.write('\n'.join(str(n) for n in random.choices(ALL_NUMS, k=size)))


def all_tests():
    """
    Creates all test files for project.
    """
    input_sizes = list(range(1, 10)) \
            + list(range(10, 100, 10)) \
            + list(range(1000, 10000, 1000)) \
            + [10000, 50000, 100000, 500000, 1000000]

    for size in input_sizes:
        print(size)
        single_test(size)
