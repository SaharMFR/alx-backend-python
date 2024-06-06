#!/usr/bin/env python3
""" Defines the type-annotated function `to_kv` """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple from string key and squared int or float value.

    Parameters:
    k: The key to put in the tuple (string).
    v: The value to put in the tuple (int or float).

    Return:
    Tuple: The created tuple from k and v.
    """
    return (k, v ** 2)
