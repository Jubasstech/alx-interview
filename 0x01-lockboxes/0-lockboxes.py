#!/usr/bin/python3

'''
    Lockboxes algorithm question.
'''


def canUnlockAll(boxes):
    '''
        Given a list of boxes, determine if you can open all of them.
    '''
    # Create a list of unlocked boxes.
    unlocked = [0]

    # Loop through the list of boxes.
    for box in boxes:
        # If the box is unlocked, then add it to the unlocked list.
        if box in unlocked:
            unlocked.append(box)

    # If the length of the unlocked list is equal to the length of the boxes list, then return True.
    if len(unlocked) == len(boxes):
        return True

    # Otherwise, return False.
    return False
