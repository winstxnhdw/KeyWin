# pylint: skip-file

from __future__ import annotations

from typing import Iterable

from keywin.generic import KeyInput, MouseInput

def send_generic_events(inputs: Iterable[KeyInput | MouseInput]) -> bool:
    """
    Summary
    -------
    a low-level event wrapper for the Windows API SendInput function

    Parameters
    ----------
    inputs (Iterable[KeyInput | MouseInput]) : a list of valid inputs

    Returns
    -------
    success (bool) : the success of the event(s)
    """
    ...

def send_mouse_events(inputs: Iterable[tuple[int, int, int, int]]) -> bool:
    """
    Summary
    -------
    a low-level mouse event wrapper for the Windows API SendInput function

    Parameters
    ----------
    inputs (Iterable[tuple[x, y, mouseData, dwFlags]]) : a list of valid mouse inputs

    Returns
    -------
    success (bool) : the success of the event(s)
    """
    ...

def send_mouse_flag(flags: int) -> bool:
    """
    Summary
    -------
    a low-level wrapper to directly send a mouse flag to the Windows API SendInput function

    Parameters
    ----------
    flags (int) : valid mouse flag(s)

    Returns
    -------
    success (bool) : the success of the event(s)
    """
    ...

def send_keyboard_events(keys: Iterable[int]) -> bool:
    """
    Summary
    -------
    a low-level keyboard event wrapper for the Windows API SendInput function

    Parameters
    ----------
    keys (Iterable[int]) : a list of valid keyboard inputs

    Returns
    -------
    success (bool) : the success of the event(s)
    """
    ...

def send_unicode_events(string: str) -> bool:
    """
    Summary
    -------
    a low-level wrapper to send unicode characters to the Windows API SendInput function

    Parameters
    ----------
    string (str) : a string of unicode characters

    Returns
    -------
    success (bool) : the success of the event(s)
    """
    ...
