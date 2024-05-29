#!/usr/bin/python3
import sys
from os import path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
filename = "add_item.json"

def add_item_to_json():
    """
    This script adds command line arguments to a JSON file.

    It first checks if the JSON file exists. If it does, it loads the contents of the file into a list.
    If the file does not exist, it initializes an empty list.

    It then extends the list with the command line arguments passed to the script.

    Finally, it saves the updated list to the JSON file.

    Args:
        None

    Returns:
        None
    """
    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(sys.argv[1:])

    save_to_json_file(my_list, filename)

add_item_to_json()
