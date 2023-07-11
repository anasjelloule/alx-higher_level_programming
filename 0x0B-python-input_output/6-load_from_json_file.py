#!/usr/bin/python3
# Anas Jelloul
"""impliment file-reading function."""
import json


def load_from_json_file(filename):
    """Construct Python object from JSON file."""
    with open(filename) as f:
        return json.load(f)
