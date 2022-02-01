#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    checks if `obj` is an instance of the specified class
    Args:
        obj (any): object to compare
        a_class (any): class to compare with the object
    Returns:
        `True` if the object is exactly an instance of the
        specified class; otherwise `False`
    """

    if type(obj) == a_class:
        return True

    return False
