#!/usr/bin/env python3
""" Defines the type-annotated function `make_multiplier` """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Multiplies multiplier by a float by a function.

    Parameters:
    multiplier: The number to multiply by a float (float).

    Return:
    Callable: The function to multiply multiplier by a float.
    """
    return lambda x: multiplier * x
