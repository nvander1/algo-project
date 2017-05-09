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

import pandas as pd
import plotly as py
import plotly.graph_objs as go

import optimal_fingerings as of


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
    parser.add_argument(
        '-g', '--graph', dest='graph', action='store_true',
        help='if present, create graphs of test data with plotly')
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
        fields = ['Input Size', 'Bottom-Up', 'Pruning']
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()

        average = lambda code: timeit(code, number=times)/times

        for filename in files:
            notes = read_notes(filename)
            size = len(notes)
            written = {'Input Size': size}
            written['Bottom-Up'] = average(lambda: of.bottom_up(notes))
            written['Pruning'] = average(lambda: of.pruning(notes))
            writer.writerow(written)
            print(f'Finished testing {filename}')
        print(f'Finished testing {len(files)} files')


def graph(results):
    """
    Graphs result data with plotly.

    Parameters
    ----------
    results : string
        Pathname of csv file with results.
    """
    data = pd.read_csv(results)
    bottom_up = go.Scatter(
        x=data['Input Size'], y=data['Bottom-Up'],
        mode='lines+markers', name='Bottom Up')

    pruning = go.Scatter(
        x=data['Input Size'], y=data['Pruning'],
        mode='lines+markers', name='Pruning')


    layout = go.Layout(
        xaxis=dict(type='log', autorange=True),
        yaxis=dict(type='log', autorange=True),
        title='Optimal Fingering Algorithms',
        plot_bgcolor='rgb(230, 230, 230)')

    fig = go.Figure(data=[bottom_up, pruning], layout=layout)

    py.offline.plot(fig, filename='Optimal_Fingering_Algorithms')


if __name__ == '__main__':
    ARGS = make_parser().parse_args()
    FILES = get_files(ARGS.directory)
    time(FILES, ARGS.output)
    if ARGS.graph:
        graph(ARGS.output)
