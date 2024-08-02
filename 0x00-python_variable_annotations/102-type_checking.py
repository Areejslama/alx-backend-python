#!/usr/bin/env python3
"""define function"""

from typing import Tuple, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    """define the function"""
    zoomed_in = tuple(item for item in lst for _ in range(factor))
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
