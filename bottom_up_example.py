"""
Demo code for presentation.
"""

from glob import glob
from timeit import timeit

import optimal_fingerings as of
import util


if __name__ == '__main__':
    bottom_up = dict()
    for filename in sorted(glob('test_files/runtime_tests/*'), key=lambda x: int(x[30:-4])):
        example = util.read_notes(filename)

        bottom_up['time'] = timeit(stmt='bottom_up["ans"] = of.bottom_up(example)', globals=globals(), number=1)
        print(f'Bottom-Up took {bottom_up["time"]} seconds on input size {filename[30:-4]} and computed length {bottom_up["ans"][0]}')
