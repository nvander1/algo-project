"""
A utility for generating test files.
"""

if __name__ == '__main__':
    import sys
    import random
    from optimal_fingerings import N2F

    ALL_NUMS = list(N2F.keys())
    SIZE = int(sys.argv[1])
    with open(f'test_files/test_{SIZE}.txt', 'w') as file:
        file.write('\n'.join(str(n) for n in random.choices(ALL_NUMS, k=SIZE)))
