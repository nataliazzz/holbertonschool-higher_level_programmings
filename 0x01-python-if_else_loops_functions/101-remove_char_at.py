#!/usr/bin/python3
def remove_char_at(str, n):
    """deletes the character at the n position of the str
    This function creates a copy of the string, deletes
    a position of the passed string and returns a string
    without the deleted position
    Parameters
    ----------
    str : str
        string from which the position needs to be removed
    n : int
        position of the string to be deleted
    Returns
    -------
    str
        copy of the string without the deleted position
    """

    new_str = ""

    for i in range(len(str)):
        if i != n:
            new_str += str[i]

    return new_str
