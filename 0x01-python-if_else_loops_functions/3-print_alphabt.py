#!/usr/bin/python3
for letter in range(ord('a'), ord('z') + 1):
    if not (chr(letter) == 'q' or chr(letter) == 'e'):
        print("{}".format(chr(letter)), end='')
