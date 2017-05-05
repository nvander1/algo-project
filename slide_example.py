"""
Demo code for presentation.
"""

from timeit import timeit

import optimal_fingerings as of


if __name__ == '__main__':
    example = [58, 59, 60]
    print(f'Example from slides: {example}')

    bottom_up = dict()
    nonpruning = dict()
    pruning = dict()

    bottom_up['time'] = timeit(stmt='bottom_up["ans"] = of.bottom_up(example)', globals=globals(), number=1)
    nonpruning['time'] = timeit(stmt='nonpruning["ans"] = of.nonpruning(example)', globals=globals(), number=1)
    pruning['time'] = timeit(stmt='pruning["ans"] = of.pruning(example)', globals=globals(), number=1)

    print(f'Bottom-Up took {bottom_up["time"]} seconds and computed {bottom_up["ans"]}')
    print(f'Nonpruning took {nonpruning["time"]} seconds and computed {nonpruning["ans"]}')
    print(f'Pruning took {pruning["time"]} seconds and computed {pruning["ans"]}')
