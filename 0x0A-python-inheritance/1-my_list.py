#!/usr/bin/python3
"""
list in asc order
"""


class MyList(list):
    """
    customize class
    """

    def print_sorted(self):
        """
        prints list
        """

        if issubclass(MyList, list):
            print(sorted(self))
