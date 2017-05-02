'''
This module contains common utilities
and constants used in different implementations
of the optimal fingering problem.
'''


from collections import defaultdict as dd
from itertools import product


'''
A mapping from fingerings to a list of notes
available at each fingering.
'''
F2N = {
    '000': [46, 53, 58, 62, 65, 68, 70, 72, 74],
    '010': [45, 52, 57, 61, 64, 67, 69, 71, 73],
    '100': [44, 51, 56, 60, 63, 66, 68, 70, 72],
    '110': [43, 50, 55, 59, 62, 65, 67, 69, 71],
    '001': [43, 50, 55, 59, 62, 65, 67, 69, 71],
    '011': [42, 49, 54, 58, 61, 64, 66, 68, 70],
    '101': [41, 48, 53, 57, 60, 63, 65, 67, 69],
    '111': [40, 47, 52, 56, 59, 62, 64, 66, 68]
    }


'''
A mapping from a note to all possible
fingerings for a note.
'''
N2F = dd(set)
for key, val in F2N.items():
    for item in val:
        N2F[item].add(key)


def dist(f_1, f_2):
    '''
    Calculates the number of moved fingers between
    two fingerings.
    '''
    return sum(x != y for x, y in zip(f_1, f_2))


'''
A mapping from pairs of fingerings to the distance between them.
'''
DIST = dict((pair, dist(*pair)) for pair in product(F2N, repeat=2))
