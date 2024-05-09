#!/usr/bin/python3
def islower(c):
    if 97 <= ord(c) <= 122:  # Check if the ASCII value of c lies between lowercase 'a' and 'z'
        return True
    else:
        return False
