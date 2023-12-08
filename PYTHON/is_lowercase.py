#!/usr/bin/python3

def islower(c):
    x = ord('a')

    while ( chr(x) != chr( ord('z') + 1) ):
        if (chr(x) == c):
            return True
        x += 1

    return False


c = "s"
print(islower(c))
