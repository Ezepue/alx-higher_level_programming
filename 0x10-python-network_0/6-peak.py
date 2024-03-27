#!/usr/bin/python3
"""contains the function find_peak"""


# def find_peak(list_of_integers):
#     """finds a peak in a list of unsorted integers"""
#     list_len = len(list_of_integers)
#     if list_len == 0:
#         return
#     m = list_len // 2
#     if (
#         (m == list_len - 1 or list_of_integers[m] >= list_of_integers[m + 1])
#         and (m == 0 or list_of_integers[m] >= list_of_integers[m - 1])
#     ):
#         return list_of_integers[m]
#     if m != list_len - 1 and list_of_integers[m + 1] > list_of_integers[m]:
#         return find_peak(list_of_integers[m + 1:])
#     return find_peak(list_of_integers[:m])

def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
