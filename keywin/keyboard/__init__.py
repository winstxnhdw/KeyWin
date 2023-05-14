from itertools import groupby

from keywin.keyboard.codes import Typables
from keywin.keyboard.exceptions import UnknownTypableException
from keywin.send_input import press_keyboard


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
    key_codes (Iterable[int]) : converted key code(s)
    """
    try:
        key_codes: list[list[int]] = []

        for key_with_modifier, group in groupby((Typables.table[character] for character in string), lambda x: isinstance(x, list)):
            group_list = list(group)

            if key_with_modifier:
                key_codes.extend(group_list)  # type: ignore

            else:
                key_codes.append(group_list)  # type: ignore

        return key_codes

    except KeyError as error:
        raise UnknownTypableException from error


def press(*keys: int):
    """
    Summary
    -------
    low-level function to press a key

    Parameters
    ----------
    *keys (int) : key code(s)
    """
    press_keyboard(keys)


def write(string: str):
    """
    Summary
    -------
    high-level function to type a string

    Parameters
    ----------
    string (str) : string to type
    """
    for key_codes in convert_to_key_code(string):
        press(*key_codes)
