#!/usr/bin/python3

def uppercase(str):
    for word in str:
        if (ord(word) > 64 and ord(word) <= 90):
            word = chr(ord(word) + 32)
        print("{}".format(word), end='')
    print()
