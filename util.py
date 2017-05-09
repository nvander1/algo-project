"""
This module contains tools that aid in testing solutions
to the optimal fingering problem.
"""

def read_notes(filename):
    """
    Creates a list of notes values from a newline separated file.

    Parameters
    ----------
    filename : string
        The input file.

    Returns
    -------
    notes : (list of int) or None
        A list of integers representing notes from the input file if
        all the notes are within range, else None.
    """
    with open(filename, 'r') as test_file:
        notes = [int(line) for line in test_file.read().splitlines()]
        return notes if all(39 < note < 75 for note in notes) else None
