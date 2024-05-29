#!/usr/bin/python3

"""
Script: 7-add_item.py
Description: This script adds command-line arguments to a Python
list and saves them to a file in JSON format.
Usage: ./7-add_item.py [arg1] [arg2] ...
"""
import json
import os.path
import sys
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
json_list = []

if os.path.exists(filename):
    json_list = load_from_json_file(filename)

for index in argv[1:]:
    json_list.append(index)

save_to_json_file(json_list, filename)