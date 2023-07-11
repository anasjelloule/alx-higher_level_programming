#!/usr/bin/python3
# Anas Jelloul
"""impliment JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an objectfile using JSON."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
