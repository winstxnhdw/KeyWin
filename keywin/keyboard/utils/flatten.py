from itertools import chain
from typing import Iterable, TypeVar

T = TypeVar('T')

def flatten(multidimensional_iterable: Iterable[Iterable[T]]) -> Iterable[T]:
    """
    Summary
    -------
    flatten a multidimensional iterable
    """
    return chain(*multidimensional_iterable)
