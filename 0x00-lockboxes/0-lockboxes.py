#!/usr/bin/python3
"""LOCKBOXES"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of list of int): A list of lists where each sublist contains keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    # PUT THE KEYS
    keys = []
    keys.extend(boxes[0])
    i = 1
    while i < len(boxes):
        if i not in keys:
            break
        else:
            keys.extend(boxes[i])
            i += 1
    if i in keys:
        return True
    else:
        return False