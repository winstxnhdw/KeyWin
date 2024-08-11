# pylint: skip-file

from __future__ import annotations

from typing import Iterable

def send_mouse_event(inputs: Iterable[tuple[int, int, int, int]]) -> bool:
    """
    Summary
    -------
    a low-level mouse event wrapper for the Windows API SendInput function

    Parameters
    ----------
    inputs (Iterable[tuple[int, int, int, int]]) : a list of valid mouse inputs
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
