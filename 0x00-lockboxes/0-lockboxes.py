#!/usr/bin/python3


def can_unlock_all(boxes):
    """
    Determines if all boxes can be unlocked starting from the first one.

    Args:
        boxes (list of list of int): A list where each sublist represents
        the keys in a box.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    # Initialize the keys list
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
