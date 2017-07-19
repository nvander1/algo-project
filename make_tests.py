"""
A utility for generating test files.
"""

__version_info__ = ('2017', '05', '10')
__version__ = '-'.join(__version_info__)

import argparse
from argparse import RawTextHelpFormatter
import os
import random

from optimal_fingerings import N2F


ALL_NUMS = list(N2F.keys())


def make_parser():
    """
    Builds an an argument parser.

    Returns
    -------
    parser : argparse.ArgumentParser
       This parser creates the usage string and handles
       command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=RawTextHelpFormatter)
    parser.add_argument(
        'sizes', metavar='N', type=int, nargs='+',
        help='number of notes in each test file')
    parser.add_argument(
        '-d', '--dir', dest='directory', required=True,
        help='the directory in which tests are placed')
    parser.add_argument(
        '-q', '--quiet', dest='quiet', required=False, action='store_true',
        help='suppress information about files created')
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s ({__version__})')
    return parser


def single_test(size, directory, quiet):
    """
    Creates a single test file with a specified number
    of notes and in a specified directory.

    Parameters
    ----------
    size : int
        The specified number of notes.

    directory : string
        The specified output directory.
    """
    filename = f'{directory}/{size}.txt'
    with open(filename, 'w') as file:
        file.write('\n'.join(str(n) for n in random.choices(ALL_NUMS, k=size)))
        if not quiet:
            print(f'Finished generating file: {filename}')


def check_directory(directory):
    """
    Creates a directory if it does not exist.

    Parameters
    ----------
    directory : string
        The directory to check and/or create.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)


def all_tests(sizes, directory, quiet):
    """
    Creates all test files of given lengths in a specified
    directory.

    Parameters
    ----------
    sizes : list of int
        A list of integers specifying the number of notes
        for each test file.
    directory : string
        The specified output directory.
    """
    check_directory(directory)
    for size in sizes:
        single_test(size, directory, quiet)
    print(f'Generated {len(sizes)} test files in: {directory}')


if __name__ == '__main__':
    ARGS = make_parser().parse_args()
    all_tests(ARGS.sizes, ARGS.directory, ARGS.quiet)
