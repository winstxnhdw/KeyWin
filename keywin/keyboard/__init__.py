from keywin.keyboard.utils import convert_to_key_code
from keywin.send_input import press_keyboard


def press(*keys: int) -> bool:
    """
    Summary
    -------
    low-level function to press a key

    Parameters
    ----------
    *keys (int) : key code(s)

    Returns
    -------
    success (bool) : the success of the event
    """
    return press_keyboard(keys)


def write(string: str) -> list[bool]:
    """
    Summary
    -------
    high-level function to type a string

    Parameters
    ----------
    string (str) : string to type

    Returns
    -------
    successes (list[bool]) : the success of the event(s)
    """
    return [press(*key_codes) for key_codes in convert_to_key_code(string)]
