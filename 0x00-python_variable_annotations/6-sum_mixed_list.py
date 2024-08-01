#!/usr/bin/env python3
"""this script return sum as float"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """define the function"""
    return sum(mxd_lst)
