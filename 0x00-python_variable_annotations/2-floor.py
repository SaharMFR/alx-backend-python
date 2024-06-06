#!/usr/bin/env python3
""" Defines the type-annotated function `floor` """

import math


def floor(n: float) -> int:
    """
    Gets the floor of a float number.

    Parameters:
    n: The number to get its floor (float).

    Return:
    int: The floor of n.
    """
    return math.floor(n)
