#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes

More info:
- Prototype: def canUnlockAll(boxes)
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False
"""
def canUnlockAll(boxes):
    """
    Description:
    Write a method that determines if all the boxes can be opened
    Arguments:
    boxes --> List of Lists, it contains the boxes with keys
    Reurn boolean
    Variables:
    keys --> List, Store the number keys to open boxes
    i --> integer
    """
    keys=[]
    keys.extend(boxes[0])
    i=1
    while(i<len(boxes)):
        if(i not in keys):
            break
        else:
            keys.extend(boxes[i])
            i+=1
    if (i in keys):
        return True
    else:
        return False
    