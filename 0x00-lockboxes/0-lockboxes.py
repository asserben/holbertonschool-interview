#!/usr/bin/python3
"""
This module provides a function to determine if all lockboxes can be unlocked.

The function `canUnlockAll` checks if all boxes in a given list can be unlocked
using the keys available in the boxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of list of int): A list of boxes, where each box contains
                                    a list of keys (integers).

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """









# #!/usr/bin/python3
# #Solve IT

# def canUnlockAll(boxes):
#     """Solve"""
#     #PUT THE KEYS
#     keys=[]
#     keys.extend(boxes[0])
#     i=1
#     while(i<len(boxes)):
#         if(i not in keys):
#             break
#         else:
#             keys.extend(boxes[i])
#             i+=1
#     if (i in keys):
#         return True
#     else:
#         return False
    