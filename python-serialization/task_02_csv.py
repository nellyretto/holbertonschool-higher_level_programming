#!/usr/bin/env python3


import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True
    except FileNotFoundError:
        return False
