#!/usr/bin/python3
'''This module contains a function canUnlockAll'''


def canUnlockAll(boxes=[[0]]):
    '''Function that determines if all the boxes can be opened'''
    keys = list(boxes[0])
    opened_boxes = [False] * len(boxes)

    opened_boxes[0] = True

    for key in keys:
        if key >= len(boxes):
            keys.remove(key)
            continue

        if opened_boxes[key] is False:
            # open the box
            opened_boxes[key] = True
            for new_key in boxes[key]:
                if opened_boxes[new_key] is False:
                    keys.append(new_key)

    return len(keys) == (len(boxes) - 1)
