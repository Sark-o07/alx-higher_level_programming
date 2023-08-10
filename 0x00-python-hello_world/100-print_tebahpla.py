#!/usr/bin/python3
for index in range(0, 26):
    letter = 122 - index
    if (index % 2 == 1):
        letter = chr(letter - 32)
    else:
        letter = chr(letter)
    print(f"{letter}", end='')
