# Determining Optimal Note Fingerings
Nikolas Vanderhoof & Andrew Chellis

## Problem Statement
We try to determine the optimal fingerings for some notes.
We define an *optimal fingering* to be a sequence of fingerings
such that the total amount of finger movement is minimal.

We use baritone fingerings in our examples, but this should
extend trivially to other wind instruments.

The baritone has three valves, and each valve can be either open
or closed. So there are eight valve configurations. We represent
each configuration as a binary 3-tuple. We compute finger movement
between two fingerings by counting number of different elements in
these 3-tuples.

### Input
A sequence of notes n1, n2, ..., nk.

### Output
A sequence of fingerings such that the sum of finger movments
between notes is minimal.

## Implementation Dependencies
- Pandas
- Plotly
