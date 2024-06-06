#!/usr/bin/env python3
""" Defines a type-annotated function `concat` """


def concat(str1: str, str2: str) -> str:
    """
    concatenates two strings.

    Parameters:
    str1: the first string to concatenate (string).
    str2: The second string to concatenate (string).

    Return:
    str: The concatenation of str1 and str2.
    """
    return str1 + str2
