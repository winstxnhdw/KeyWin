# pylint: skip-file

from typing import Iterable

def send_mouse_event(inputs: Iterable[list[int]]) -> bool:
    """
    Summary
    -------
    a low-level mouse event wrapper for the Windows API SendInput function

    Parameters
    ----------
    inputs (Iterable[list[int]]) : a list of valid mouse inputs
    """
    ...


def press_keyboard(keys: Iterable[int]) -> bool:
    """
    Summary
    -------
    a low-level keyboard event wrapper for the Windows API SendInput function

    Parameters
    ----------
    keys (Iterable[int]) : a list of valid keyboard inputs
    """
    ...
