"""
API for wc package
"""

import collections
import os

file_info = collections.namedtuple('file_info', 'lines words')


def get_file_info(file_):
    """
    Get number of lines and words in file

    :param file_: Name of file to inspect
    :returns: file_info tuple
    """

    lines = 0
    words = 0

    with open(file_, 'rb') as file_obj:
        for line in file_obj:
            lines += 1
            words += len(line.split())

    return file_info(lines, words)


def get_directory_info(dir_):
    """
    Get number of lines and words in all files in directory

    :param dir_: Name of directory to inspect
    :returns: List of file_info tuples for each file in directory
    """

    results = []

    for item in os.listdir(dir_):
        file_ = os.path.join(dir_, item)
        if not os.path.isfile(file_):
            continue

        results.append((file_, get_file_info(file_)))

    return results
