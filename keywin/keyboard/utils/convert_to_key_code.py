from itertools import groupby

from keywin.keyboard.codes import Typables
from keywin.keyboard.exceptions import UnknownTypableException


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

        for key, group in groupby((Typables.table[character] for character in string), type):
            if key == list:
                key_codes.extend(group)  # pyright: ignore[reportGeneralTypeIssues]

            else:
                key_codes.append(list(group))  # pyright: ignore[reportGeneralTypeIssues]

        return key_codes

    except KeyError as error:
        raise UnknownTypableException from error
