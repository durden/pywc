"""
Script to mostly mimic the `wc` command in Unix on all platforms
"""

import argparse
import collections
import os
import sys

file_info = collections.namedtuple('file_info', 'lines words')


def get_file_info(file_):
    lines = 0
    words = 0

    with open(file_, 'r', encoding='utf-8') as file_obj:
        for line in file_obj:
            lines += 1
            words += len(line.split())

    return file_info(lines, words)


def parse_args():
    parser = argparse.ArgumentParser(
        description='Count lines/words in files or directory')

    parser.add_argument(
        'arg', action='store',
        help='File or directory to count lines/words for')

    parser.add_argument(
        '-w', dest='count_words', action='store_true', default=False,
        help='Show number of words in file(s)')

    parser.add_argument(
        '-l', dest='count_lines', action='store_true', default=False,
        help='Show number of lines in file(s)')

    # Using vars() to turn namespace object returned by parse_args() into a
    # dict.
    args = vars(parser.parse_args())

    # Mimic wc command by printing both of these if there are no other
    # arguments
    if not args['count_words'] and not args['count_lines']:
        args['count_words'] = True
        args['count_lines'] = True

    return args


def main(arg, count_words, count_lines):
    results = []

    if os.path.isfile(arg):
        results.append((arg, get_file_info(arg)))
    else:
        for item in os.listdir(arg):
            file_ = os.path.join(arg, item)
            if not os.path.isfile(file_):
                continue

            results.append((file_, get_file_info(file_)))

    for arg, result in results:
        if count_lines:
            print(f'    {result.lines}', end='')

        if count_words:
            print(f'    {result.words}', end='')

        print(f'    {arg}')


args = parse_args()
main(args['arg'], args['count_words'], args['count_lines'])
