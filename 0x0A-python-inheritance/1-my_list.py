#!/usr/bin/python3
"""
module that prints list in ascending order
"""


class MyList(list):
    """
    class to customize the list
    """

    def print_sorted(self):
        """
        list in ascending order
        sort list and then prints the output
        """

        if issubclass(MyList, list):
            print(sorted(self))
