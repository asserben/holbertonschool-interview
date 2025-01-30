#!/usr/bin/python3


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
    #PUT THE KEYS
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
