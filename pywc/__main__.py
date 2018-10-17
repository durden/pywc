"""
CLI interface to wc package
"""

import argparse
import os
import sys

from gooey import Gooey
from gooey.python_bindings.gooey_decorator import IGNORE_COMMAND

from pywc import api


def gui():
    """
    Usually Gooey is used as a decorator, but in our case we want to provide
    the GUI as an option.
    """

    # This is a perfect setup for functools.partial, but Gooey wants a real
    # function not a partial object
    def cli_only():
        return cli(allow_gui_option=False)

    return Gooey(cli_only, show_success_modal=False)()


def cli(allow_gui_option=True):
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

    if allow_gui_option:
        parser.add_argument(
            '-g', dest='use_gui', action='store_true', default=False,
            help='Use GUI to run application')

    # Gooey puts this in when it re-runs itself, but we're not using this
    # option because we want the default of the app to run without a GUI. Gooey
    # defaults to using the GUI, not the other way around.
    if IGNORE_COMMAND in sys.argv:
        sys.argv.remove(IGNORE_COMMAND)

    # Using vars() to turn namespace object returned by parse_args() into a
    # dict.
    args = vars(parser.parse_args())

    if args['use_gui']:
        sys.argv.remove('-g')
        # Let Gooey run us
        gui()
        return

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