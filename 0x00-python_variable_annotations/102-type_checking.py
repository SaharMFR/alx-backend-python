#!/usr/bin/env python3
""" Defines the function `zoom_array` to be annotated """

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ The function to be annotated """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)