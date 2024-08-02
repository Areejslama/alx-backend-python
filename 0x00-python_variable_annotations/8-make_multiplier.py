#!/usr/bin/env python3
"""this script define multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """define a function"""
    def func(x: float) -> float:
        """define another function"""
        return x * multiplier
    return func
