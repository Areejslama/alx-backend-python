#!/usr/bin/env python3
"""this script define a duck type"""

from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """define the function"""
    if lst:
        return lst[0]
    else:
        return None
