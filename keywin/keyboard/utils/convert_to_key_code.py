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

        for key_with_modifier, group in groupby((Typables.table[character] for character in string), lambda x: isinstance(x, list)):
            group_list = list(group)

            if key_with_modifier:
                key_codes.extend(group_list)

            else:
                key_codes.append(group_list)

        return key_codes

    except KeyError as error:
        raise UnknownTypableException from error
