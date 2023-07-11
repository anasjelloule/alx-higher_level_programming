#!/usr/bin/python3
# Anas Jelloul
"""Impliment class int."""


class MyInt(int):
    """Int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
