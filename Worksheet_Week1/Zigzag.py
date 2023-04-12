"""
Defines the function zigzag()

Passes throught the parameters a, b, and c to check if it meets the conditions.
"""
def zigzag(a, b, c):
    # If these conditions are met it is a zigzag and returns True.
    if a<b>c or a>b<c:
        return True
    # If they are not met it is not a zigzag and returns False.
    else:
        return False
