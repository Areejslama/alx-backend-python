#!/usr/bin/env python3
"""this script return float"""
from typing import Union, Tuple


def to_kv(k: int, v: Union[int, float]) -> Tuple[int, float]:
    """define the function"""
    return k, float(v * v)
