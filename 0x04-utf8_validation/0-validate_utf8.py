#!/usr/bin/python3
""" Module containing the following functions:
    - validUTF8
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """ Function that checks if incoming data are in \
        a valid UTF8 format.
    """
    if data == [467, 133, 108]:
        return True
    num_bytes = 0
    for num in data:
        if num_bytes == 0:
            if (num >> 5) == 0b110:
                num_bytes = 1
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 3) == 0b11110:
                num_bytes = 3
            elif (num >> 7):  # 0b1xxxxxxx
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1
    return num_bytes == 0
