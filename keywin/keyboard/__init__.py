from typing import Iterable

from keywin.keyboard.codes import Typables
from keywin.keyboard.exceptions import UnknownTypableException
from keywin.keyboard.utils import flatten
from keywin.send_input import press_keyboard


def convert_to_key_code(string: str) -> Iterable[int]:
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
        return flatten(Typables.table[character] for character in string)

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
    press(*convert_to_key_code(string))
