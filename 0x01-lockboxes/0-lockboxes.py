#!/usr/bin/python3
'''This module contains a function canUnlockAll'''


def canUnlockAll(boxes):
    '''Function that determines if all the boxes can be opened'''
    keys = list(boxes[0])
    opened_boxes = [False] * len(boxes)

    opened_boxes[0] = True

    i = 0
    while i < len(keys):
        key = keys[i]
        if key < len(boxes) and not opened_boxes[key]:
            # open the box
            opened_boxes[key] = True
            for new_key in boxes[key]:
                if not opened_boxes[new_key]:
                    keys.append(new_key)
        i += 1

    return all(opened_boxes)
