"""
Script to mostly mimic the `wc` command in Unix on all platforms
"""

import os
import sys


def count_lines(file_):
    with open(file_, 'r', encoding='utf-8') as file_obj:
        count = 0
        for _ in file_obj:
            count += 1

    return count


arg = sys.argv[1]

if os.path.isfile(arg):
    print(count_lines(arg))
else:
    for item in os.listdir(arg):
        file_ = os.path.join(arg, item)
        if not os.path.isfile(file_):
            continue

        num_lines = count_lines(file_)
        print(f'{file_}: {num_lines}')
