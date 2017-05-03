"""
A state-space tree pruning solution to the optimal fingering problem.
"""


import sys
from collections import defaultdict, deque
from optimal_fingerings import N2F
from Node import Node
from util import read_notes, time


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
        for key in choices:
            items.append(min(choices[key]))
        index += 1
    return min(items)


if __name__ == '__main__':
    TIMER = time(pruning)
    print(*TIMER(read_notes(sys.argv[1])))
