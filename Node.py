"""
This module contains an implementation of a state-space-tree Node.
"""

from optimal_fingerings import DIST, N2F


class Node():
    """
    A Node in the state-space-tree for the optimal fingering problem.

    Attributes
    ----------
    comb : string
        The string representation of the valve combination.

    fingerings : list of strings
        The fingerings chosen up to and including this Node.

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
        while current is not None:
            fingerings.append(current.comb)
            current = current.parent
        fingerings.reverse()
        return f'{(self.cost, fingerings)}'
