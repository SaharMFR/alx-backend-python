#!/usr/bin/env python3
""" Defines a function `element_length` to be annotated """

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ The function to be annotated """
    return [(i, len(i)) for i in lst]
