from __future__ import annotations

from typing import Literal, TypedDict

from keywin.send_input import send_generic_events


class MouseInput(TypedDict):
    """
    Summary
    -------
    a dictionary for the mouse input

    Attributes
    ----------
    x (int) : the x-coordinate
    y (int) : the y-coordinate
    data (int) : the mouse data
    flags (int) : the mouse flags
    """

    x: int
    y: int
    data: int
    flags: int


class KeyInput(TypedDict):
    """
    Summary
    -------
    a dictionary for the key input

    Attributes
    ----------
    key (int) : the key code
    release (Literal[False, 0x02]) : the key release flag
    """

    key: int
    release: Literal[False, 0x02]


def send_input(*inputs: KeyInput | MouseInput) -> bool:
    """
    Summary
    -------
    a low-level function to send generic input events

    Parameters
    ----------
    *inputs (KeyInput | MouseInput) : input event(s)

    Returns
    -------
    success (bool) : the success of the event
    """
    return send_generic_events(inputs)
