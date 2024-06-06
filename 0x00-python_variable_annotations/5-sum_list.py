#!/usr/bin/env python3
""" Defines the type-annotated function `sum_list` """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Caculates the sum of floats in a list.

    Parameters:
    input_list: The list to calculate the sum of its elements (list[float]).

    Return:
    float: The sum of the elements of input_list.
    """
    return sum(input_list)
