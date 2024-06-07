#!/usr/bin/env python3
"""
Defintes the function `safe_first_element` to be augmented with
the correct duck_typed annotations.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    The function to be augmented with the correct duck_typed annotations.
    """
    if lst:
        return lst[0]
    else:
        return None
