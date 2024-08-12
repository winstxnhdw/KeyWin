from __future__ import annotations

from keywin.mouse.mouse_code import MouseCode
from keywin.send_input import send_mouse_events, send_mouse_flag


def create_event(flags: int, x: int = 0, y: int = 0, mouse_data: int = 0) -> tuple[int, int, int, int]:
    """
    Summary
    -------
    helper function to create a mouse event

    Parameters
    ----------
    flags (int) : flag to use for the mouse event
    x (int?) : generic x-axis value
    y (int?) : generic y-axis value
    mouse_data (int?) : data to use for the mouse event

    Return
    --------
    event (tuple[int, int, int, int]) : the mouse event
    """
    return (x, y, mouse_data, flags)


def send_events(*inputs: tuple[int, int, int, int]) -> bool:
    """
    Summary
    -------
    low-level function to send mouse events

    Parameters
    ----------
    *inputs (tuple[int, int, int, int]) : mouse event(s)

    Return
    --------
    success (bool) : the success of the event
    """
    return send_mouse_events(inputs)


def left_click() -> bool:
    """
    Summary
    -------
    return click the left mouse button

    Return
    --------
    success (bool) : the success of the event
    """
    return send_mouse_flag(MouseCode.MOUSE_LEFT_CLICK)


def right_click() -> bool:
    """
    Summary
    -------
    return click the right mouse button

    Return
    --------
    success (bool) : the success of the event
    """
    return send_mouse_flag(MouseCode.MOUSE_RIGHT_CLICK)


def middle_click() -> bool:
    """
    Summary
    -------
    return click the middle mouse button

    Return
    --------
    success (bool) : the success of the event
    """
    return send_mouse_flag(MouseCode.MOUSE_MIDDLE_CLICK)


def xbutton1_click() -> bool:
    """
    Summary
    -------
    return click `xbutton1`

    Return
    --------
    success (bool) : the success of the event
    """
    return send_events((0, 0, MouseCode.XBUTTON1, MouseCode.MOUSE_XBUTTON1_CLICK))


def xbutton2_click() -> bool:
    """
    Summary
    -------
    return click `xbutton2`

    Return
    --------
    success (bool) : the success of the event
    """
    return send_events((0, 0, MouseCode.XBUTTON2, MouseCode.MOUSE_XBUTTON2_CLICK))


def left_press() -> bool:
    """
    Summary
    -------
    press the left mouse button

    Return
    --------
    success (bool) : the success of the event
    """
    return send_mouse_flag(MouseCode.MOUSEEVENTF_LEFTDOWN)


def left_release() -> bool:
    """
    Summary
    -------
    release the left mouse button

    Return
    --------
    success (bool) : the success of the event
    """
    return send_mouse_flag(MouseCode.MOUSEEVENTF_LEFTUP)


def right_press() -> bool:
    """
    Summary
    -------
    press the right mouse button

    Return
    --------
    success (bool) : the success of the event
    """
    return send_mouse_flag(MouseCode.MOUSEEVENTF_RIGHTDOWN)


def right_release() -> bool:
    """
    Summary
    -------
    release the right mouse button

    Return
    --------
    success (bool) : the success of the event
    """
    return send_mouse_flag(MouseCode.MOUSEEVENTF_RIGHTUP)


def middle_press() -> bool:
    """
    Summary
    -------
    press the middle mouse button

    Return
    --------
    success (bool) : the success of the event
    """
    return send_mouse_flag(MouseCode.MOUSEEVENTF_MIDDLEDOWN)


def middle_release() -> bool:
    """
    Summary
    -------
    release the middle mouse button

    Return
    --------
    success (bool) : the success of the event
    """
    return send_mouse_flag(MouseCode.MOUSEEVENTF_MIDDLEUP)


def xbutton1_press() -> bool:
    """
    Summary
    -------
    press `xbutton1`

    Return
    --------
    success (bool) : the success of the event
    """
    return send_events((0, 0, MouseCode.XBUTTON1, MouseCode.MOUSEEVENTF_XDOWN))


def xbutton1_release() -> bool:
    """
    Summary
    -------
    release `xbutton1`

    Return
    --------
    success (bool) : the success of the event
    """
    return send_events((0, 0, MouseCode.XBUTTON1, MouseCode.MOUSEEVENTF_XUP))


def xbutton2_press() -> bool:
    """
    Summary
    -------
    press `xbutton2`

    Return
    --------
    success (bool) : the success of the event
    """
    return send_events((0, 0, MouseCode.XBUTTON2, MouseCode.MOUSEEVENTF_XDOWN))


def xbutton2_release() -> bool:
    """
    Summary
    -------
    release `xbutton2`

    Return
    --------
    success (bool) : the success of the event
    """
    return send_events((0, 0, MouseCode.XBUTTON2, MouseCode.MOUSEEVENTF_XUP))


def move_relative(x: int, y: int) -> bool:
    """
    Summary
    -------
    move mouse relative to the current position

    Parameters
    ----------
    x (int) : amount of pixels to move the mouse on the x-axis
    y (int) : amount of pixels to move the mouse on the y-axis

    Return
    --------
    success (bool) : the success of the event
    """
    return send_events((x, y, 0, MouseCode.MOUSEEVENTF_MOVE))


def move(x: int, y: int) -> bool:
    """
    Summary
    -------
    move mouse to an absolute position

    Parameters
    ----------
    x (int) : coordinate on the x-axis to move the mouse to
    y (int) : coordinate on the y-axis to move the mouse to

    Return
    --------
    success (bool) : the success of the event
    """
    return send_events((x, y, 0, MouseCode.MOUSE_MOVE_ABSOLUTE))


def scroll(scroll_delta: int) -> bool:
    """
    Summary
    -------
    scroll the vertical mouse wheel

    Parameters
    ----------
    scroll_delta (int) : amount to scroll the mouse wheel

    Return
    --------
    success (bool) : the success of the event
    """
    return send_events((0, 0, scroll_delta, MouseCode.MOUSEEVENTF_WHEEL))


def scroll_horizontal(scroll_delta: int) -> bool:
    """
    Summary
    -------
    scroll the horizontal mouse wheel

    Parameters
    ----------
    scroll_delta (int) : amount to scroll the mouse wheel

    Return
    --------
    success (bool) : the success of the event
    """
    return send_events((0, 0, scroll_delta, MouseCode.MOUSEEVENTF_HWHEEL))
