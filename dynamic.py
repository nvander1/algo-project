"""
Dynamic programming solutions to the optimal fingering problem.
"""

from collections import deque
import sys

from pandas import DataFrame

from optimal_fingerings import F2N, DIST, N2F
from util import read_notes, time


def make_table():
    """
    Creates an empty table whose rows and columns are indexed by fingerings.
    """
    columns = F2N.keys()
    return DataFrame(columns=columns, index=columns)


def bottom_up(notes):
    """
    Computes the solution to the optimal fingering problem in a bottom-up manner.
    """
    notes = notes
    tables = [make_table() for i in range(len(notes))]
    tables[0][:] = 0
    prev_choices = N2F[notes[0]]

    for i in range(1, len(notes)):
        choices = N2F[notes[i]]
        for prev_choice in prev_choices:
            for choice in choices:
                tables[i][prev_choice][choice] =\
                DIST[prev_choice, choice] + tables[i-1].loc[prev_choice].min()
        prev_choices = choices

    fingerings = deque([tables[-1].min(axis=1).argmin()])
    last_fingering = tables[-1].min(axis=0).argmin()
    for i in range(len(notes)-2, 0, -1):
        fingerings.appendleft(last_fingering)
        last_fingering = tables[i].loc[last_fingering].argmin()
    fingerings.appendleft(last_fingering)

    return int(tables[-1].min().min()), list(fingerings)

if __name__ == '__main__':
    TIMER = time(bottom_up)
    print(*TIMER(read_notes(sys.argv[1])))
