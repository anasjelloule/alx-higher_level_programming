#!/usr/bin/python3
# Anas Jelloul
"""Impliment  inherited list class MyList."""


class MyList(list):
    """Implement sorted printing built-in list class."""

    def print_sorted(self):
        """Print list in sorted order ascended."""
        print(sorted(self))
