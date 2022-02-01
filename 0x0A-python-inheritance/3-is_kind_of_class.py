#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    checks if `obj` is the same class from `a_class`
    Args:
        obj (any): object to compare
        a_class (any): class to compare with the object
    Returns:
        `True` if object is an instance or inherit from the
        specified class; otherwise `False`
    """

    return isinstance(obj, a_class)
