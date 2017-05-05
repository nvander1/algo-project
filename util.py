"""
This module contains tools that aid in testing solutions
to the optimal fingering problem.
"""

def read_notes(filename):
    """
    Creates a list of notes values from a newline separated file.
    """
    with open(filename, 'r') as test_file:
        notes = [int(line) for line in test_file.read().splitlines()]
        return notes if all(39 < note < 75 for note in notes) else None
