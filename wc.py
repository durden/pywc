"""
Script to mostly mimic the `wc` command in Unix on all platforms
"""

import sys

with open(sys.argv[1], 'r', encoding='utf-8') as file_obj:
    count = 0
    for _ in file_obj:
        count += 1

print(count)
