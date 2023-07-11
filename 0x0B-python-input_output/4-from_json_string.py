#!/usr/bin/python3
# Anas Jelloul
"""Impliment JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return JSON string."""
    return json.loads(my_str)
