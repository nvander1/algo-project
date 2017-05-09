"""
Runs tests on optimal fingering solutions, and saves
results to a csv.
"""

import argparse
from argparse import RawTextHelpFormatter
import csv
import glob
import os
from timeit import timeit

import optimal_fingerings as of
import util


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
        '-d', '--dir', metavar='INPUT_DIR', required=True, dest='directory',
        help='a directory with generated test files')
    parser.add_argument(
        '-o', '--output', metavar='OUTPUT', default='results.csv', dest='output',
        help='a filename to save csv file')
    return parser


def get_files(directory):
    """
    Gets test files from a directory.

    Paramters
    ---------
    directory : string
        The name of the directory that contains only testfiles.

    Returns
    -------
    list
        A list of test files in the directory.
    """
    return sorted(glob.glob(f'{directory}/*'), key=os.path.getsize)


def time(files, output, times=1):
    """
    Times Bottom-Up and Pruning methods on test files and saves as a csv.

    Parameters
    ----------
    files : list of strings
        A list of files to test.
    output : string
        The path at which to save the results.
    times : int
        How many times to execute each test.
    """
    with open(output, 'w') as csv_file:
        fields = ['Input Size', 'Bottom-Up Time', 'Pruning Time']
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()

        average = lambda code: timeit(code, number=times)/times

        for filename in files:
            notes = util.read_notes(filename)
            size = len(notes)
            written = {'Input Size': size}
            written['Bottom-Up Time'] = average(lambda: of.bottom_up(notes))
            written['Pruning Time'] = average(lambda: of.pruning(notes))
            writer.writerow(written)
            print(f'Finished testing {filename}')
        print(f'Finished testing {len(files)} files')


if __name__ == '__main__':
    ARGS = make_parser().parse_args()
    FILES = get_files(ARGS.directory)
    time(FILES, ARGS.output)
