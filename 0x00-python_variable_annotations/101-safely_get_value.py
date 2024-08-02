#!/usr/bin/env python3
"""this script define function"""

from typing import TypeVar, Mapping, Any, Optional, Union
T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Optional[T]
        ) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
