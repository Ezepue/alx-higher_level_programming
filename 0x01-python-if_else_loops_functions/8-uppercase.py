#!/usr/bin/python3
def uppercase(str):
    for character in str:
        if (ord(character) >= ord('a') and ord(character) <= ord('z')):
            character = chr(ord(character) - 32)
        print("{}".format(character), end='')
    print("{}".format(''))
