#!/usr/bin/env python3
""" Defines the type-annotated function `sum_mixed_list` """

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Caculates the sum of integers and floats in a list.

    Parameters:
    mxd_list: The list to calculate the sum of its items (List[int, float]).

    Return:
    float: The sum of the items of mxd_list.
    """
    return sum(mxd_list)
