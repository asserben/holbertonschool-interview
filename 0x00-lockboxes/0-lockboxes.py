#!/usr/bin/python3
#Solve IT
def canUnlockAll(boxes):
    """Solve"""
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
    