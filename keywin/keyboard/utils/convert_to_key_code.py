from functools import lru_cache
from itertools import chain, groupby

from keywin.keyboard.codes import Typables
from keywin.keyboard.exceptions import UnknownTypableException


@lru_cache(maxsize=None)
def convert_to_key_code(string: str) -> list[list[int]]:
    """
    Summary
    -------
    convert a string to key code(s)

    Parameters
    ----------
    string (str) : string to convert

    Returns
    -------
    key_codes (list[list[int]]) : converted key code(s)
    """
    try:
        key_codes: list[list[int]] = []

        for multi_key, group in groupby(
            (Typables.table[character] for character in string), lambda codes: len(codes) > 1
        ):
            if multi_key:
                key_codes.extend(group)

            else:
                key_codes.append(list(chain.from_iterable(group)))

        return key_codes

    except KeyError as error:
        raise UnknownTypableException from error
