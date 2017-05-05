"""
Demo code for presentation.
"""

from glob import glob
from timeit import timeit

import optimal_fingerings as of
import util


if __name__ == '__main__':
    pruning = dict()
    for filename in sorted(glob('test_files/runtime_tests/*'), key=lambda x: int(x[30:-4])):
        example = util.read_notes(filename)

        pruning['time'] = timeit(stmt='pruning["ans"] = of.pruning(example)', globals=globals(), number=1)

        print(f'Pruning took {pruning["time"]} seconds on input size {filename[30:-4]} and computed length {pruning["ans"].cost}')
