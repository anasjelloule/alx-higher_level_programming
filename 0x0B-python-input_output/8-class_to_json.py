#!/usr/bin/python3
# Anas Jelloul
"""Impliment class-to-JSON function."""


def class_to_json(obj):
    """Return dictionary_of a simple data structure."""
    return obj.__dict__
