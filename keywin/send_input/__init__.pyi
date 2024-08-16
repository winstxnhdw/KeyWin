# pylint: skip-file

from __future__ import annotations

def send_mouse_events(inputs: tuple[tuple[int, int, int, int], ...]) -> bool:
    """
    Summary
    -------
    a low-level mouse event wrapper for the Windows API SendInput function

    Parameters
    ----------
    inputs (Iterable[tuple[dwFlags, x, y, mouseData]]) : a list of valid mouse inputs

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

def send_keyboard_events(keys: tuple[tuple[int, int, int], ...]) -> bool:
    """
    Summary
    -------
    a low-level keyboard event wrapper for the Windows API SendInput function

    Parameters
    ----------
    keys (Iterable[tuple[wVk, wScan, dwFlags]]) : a list of valid keyboard inputs

    Returns
    -------
    success (bool) : the success of the event(s)
    """
    ...

def send_keyboard_press_events(keys: tuple[int, ...]) -> bool:
    """
    Summary
    -------
    a low-level wrapper to send a keyboard press event to the Windows API SendInput function

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
