#!/usr/bin/python3
''' Module for log parsing '''
import sys
from signal import signal, SIGINT
import re
from datetime import datetime


def log_parse(file_line, file_size, curr_stats):
    ''' Function to parse log file '''
    if not validate_file_line(file_line):
        return file_size
    file_size += int(file_line.split()[-1])
    status_code = file_line.split()[-2]
    curr_stats[status_code] = curr_stats.get(status_code, 0) + 1
    return file_size


def print_log(file_size, curr_stats):
    ''' Function to print log '''
    print('File size: {}'.format(file_size))
    for key in sorted(curr_stats.keys()):
        print('{}: {}'.format(key, curr_stats[key]))


def validate_file_line(file_line):
    ''' Function to validate file line '''
    re_e = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    line = '{}\\-{}{}{}{}\\s*'.format(
        re_e[0], re_e[1], re_e[2], re_e[3], re_e[4])
    check = re.fullmatch(line, file_line)
    return 1 if check else 0


if __name__ == "__main__":
    file_size = 0
    line_count = 0
    curr_stats = {}
    # file = ""
    # with open('log_test.txt', encoding="utf-8") as f:
    #     file = f.readlines()
    try:
        # for line in file:
        while True:
            line = input()
            file_size = log_parse(line, file_size, curr_stats)
            line_count += 1
            if line_count == 10:
                line_count = 0
                print_log(file_size, curr_stats)
    except (KeyboardInterrupt, EOFError):
        print_log(file_size, curr_stats)
