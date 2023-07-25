from keywin.keyboard.utils import convert_to_key_code
from keywin.send_input import press_keyboard


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
