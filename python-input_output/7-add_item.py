#!/usr/bin/python3

"""
Script: 7-add_item.py
Description: This script adds command-line arguments to a Python
list and saves them to a file in JSON format.
Usage: ./7-add_item.py [arg1] [arg2] ...
"""
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    my_list = load_from_json_file('add_item.json')
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, 'add_item.json')
except Exception:
    my_list = sys.argv[1:]
    save_to_json_file(my_list, 'add_item.json')
