"""
A state-space tree brute force solution to the optimal fingering problem.
"""


import sys
from collections import deque
from optimal_fingerings import N2F
from Node import Node
from util import read_notes, time


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

if __name__ == '__main__':
    TIMER = time(nonpruning)
    print(*TIMER(read_notes(sys.argv[1])))
