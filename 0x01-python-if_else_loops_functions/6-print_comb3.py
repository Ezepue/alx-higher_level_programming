#!/usr/bin/python3
for i in range(9):
    for j in range(i + 1, 10):
        print("{}".format(i), end='')
        if i == 8:
            print("{}".format(j))
        else:
            print("{}".format(j), end=", ")
