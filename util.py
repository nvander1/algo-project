"""
This module contains tools that aid in testing solutions
to the optimal fingering problem.
"""

from timeit import default_timer as timer

def time(func):
    """
    Creates a new function that times the function and returns
    a tuple containing the function's result and its execution time
    """
    def wrapped(notes): # pylint: disable=missing-docstring
        start = timer()
        func_result = func(notes)
        end = timer()
        return func_result, end-start
    return wrapped

def read_notes(filename):
    """
    Creates a list of notes values from a newline separated file.

    >>> read_notes('./test_files/test_3.txt')
    [59, 60, 61]
    >>> read_notes('./test_files/test_22.txt')
    [65, 59, 48, 47, 60, 55, 51, 70, 71, 65, 63, \
66, 70, 54, 53, 52, 56, 52, 53, 70, 63, 66]
    >>> read_notes('./test_files/test_42.txt')
    [51, 55, 59, 62, 48, 47, 57, \
60, 63, 66, 70, 71, 65, 59, \
48, 47, 60, 55, 51, 70, 71, \
65, 63, 66, 70, 54, 53, 52, \
56, 57, 58, 59, 60, 63, 66, \
70, 71, 65, 59, 48, 47, 60]
    >>> read_notes('./test_files/below_range.txt') is None
    True
    >>> read_notes('./test_files/above_range.txt') is None
    True
    """
    with open(filename, 'r') as test_file:
        notes = [int(line) for line in test_file.read().splitlines()]
        return notes if all(39 < note < 75 for note in notes) else None


if __name__ == '__main__':
    import doctest
    doctest.testmod()
