#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

try:
    arguments = load_from_json_file(filename)
except Exception:
    arguments = []

for item in sys.argv[1:]:
    arguments.append(str(item))

save_to_json_file(arguments, filename)
