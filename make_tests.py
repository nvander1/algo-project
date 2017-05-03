"""
A utility for generating test files.
"""
import sys
import random

from optimal_fingerings import N2F

ALL_NUMS = list(N2F.keys())

def single_test(size):
    """
    Creates a single test file of specified length.
    """
    with open(f'test_files/test_{size}.txt', 'w') as file:
        file.write('\n'.join(str(n) for n in random.choices(ALL_NUMS, k=size)))

if __name__ == '__main__':
    ARGC = len(sys.argv)
    if ARGC == 2:
        single_test(int(sys.argv[1]))
    elif ARGC == 4:
        START = int(sys.argv[2])
        SCALE = int(sys.argv[3])
        for i in range(1, 1+int(sys.argv[1])):
            single_test(SCALE * START ** i)
            print(SCALE * START ** i)
