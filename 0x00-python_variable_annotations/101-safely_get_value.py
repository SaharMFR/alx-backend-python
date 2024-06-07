#!/usr/bin/env python3
""" Defines the function `safely_get_value` to be annotated """

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')
D = Union[T, None]
R = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: D = None) -> R:
    """ The function to be annotated """
    if key in dct:
        return dct[key]
    else:
        return default
