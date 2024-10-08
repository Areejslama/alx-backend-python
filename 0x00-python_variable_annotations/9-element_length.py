#!/usr/bin/env python3
"""this script definr a function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """define the function"""
    return [(i, len(i)) for i in lst]
