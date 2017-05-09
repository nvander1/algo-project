"""
This module contains different implementations of
solutions to the optimal fingering problem.
"""


from collections import defaultdict
from collections import deque
from itertools import product

from pandas import DataFrame


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
"""
A mapping from fingerings to a list of notes
available at each fingering.
"""


N2F = defaultdict(set)
"""
A mapping from a note to all possible
fingerings for a note.
"""
for key, val in F2N.items():
    for item in val:
        N2F[item].add(key)


def dist(f_1, f_2):
    """
    Calculates the number of moved fingers between
    two fingerings.
    """
    return sum(x != y for x, y in zip(f_1, f_2))


DIST = dict((pair, dist(*pair)) for pair in product(F2N, repeat=2))
"""
A mapping from pairs of fingerings to the distance between them.
"""

class Node():
    """
    A Node in the state-space-tree for the optimal fingering problem.

    Attributes
    ----------
    comb : string
        The string representation of the valve combination.

    parent : Node
        The Node above this in the tree.

    index : integer
        This Node's level in the tree.

    cost : integer
        The number of finger movements used to reach this configuration.
    """
    def __init__(self, comb, parent=None):
        self.comb = comb
        self.parent = parent
        if parent is None:
            self.index = 0
            self.cost = 0
        else:
            self.index = parent.index + 1
            self.cost = parent.cost + DIST[comb, parent.comb]

    def choices(self, notes):
        """
        Gets the choices present (children) at this Node.
        """
        return N2F[notes[self.index]]

    def __eq__(self, other):
        return self.cost == other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __str__(self):
        fingerings = [self.comb]
        current = self.parent
        while current.parent is not None:
            fingerings.append(current.comb)
            current = current.parent
        fingerings.reverse()
        return f'{(self.cost, fingerings)}'


def nonpruning(notes):
    """
    Computes the solution to the optimal fingering problem in a top-down
    manner through brute force expansion of a state-space tree.
    """
    items = deque()
    for comb in N2F[notes[0]]:
        ins = Node(comb)
        items.append(ins)
    while items:
        cur = items.popleft()
        if cur.index == len(notes):
            items.append(cur)
            break
        for comb in cur.choices(notes):
            ins = Node(comb, parent=cur)
            items.append(ins)
    return min(items)


def pruning(notes):
    """
    Computes the solution to the optimal fingering problem in a top-down
    manner by pruning a state-space tree.
    """
    items = deque()
    for comb in N2F[notes[0]]:
        ins = Node(comb)
        items.append(ins)
    index = 0
    while index < len(notes):
        choices = defaultdict(list)
        while items:
            cur = items.popleft()
            for comb in cur.choices(notes):
                ins = Node(comb, parent=cur)
                choices[comb].append(ins)
        for choice in choices:
            items.append(min(choices[choice]))
        index += 1
    return min(items)


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

# Traverse tables in reverse to build solution
    fingerings = deque([tables[-1].min(axis=1).argmin()])
    last_fingering = tables[-1].min(axis=0).argmin()
    for i in range(len(notes)-2, 0, -1):
        fingerings.appendleft(last_fingering)
        last_fingering = tables[i].loc[last_fingering].argmin()
    fingerings.appendleft(last_fingering)

    return int(tables[-1].min().min()), list(fingerings)
