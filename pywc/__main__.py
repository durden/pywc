"""
CLI interface to wc package
"""

import argparse
import os
import sys

from pywc import api


def cli():
    parser = argparse.ArgumentParser(
        prog='pywc',
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

    if os.path.isfile(args['arg']):
        results = [(args['arg'], api.get_file_info(args['arg']))]
    else:
        results = api.get_directory_info(args['arg'])

    for arg, result in results:
        if args['count_lines']:
            print(f'    {result.lines}', end='')

        if args['count_words']:
            print(f'    {result.words}', end='')

        print(f'    {arg}')


if __name__ == '__main__':
    cli()
