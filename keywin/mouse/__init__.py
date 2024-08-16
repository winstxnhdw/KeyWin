from __future__ import annotations

from keywin.mouse.helpers.mouse_event import MouseEvent
from keywin.mouse.mouse_code import MouseCode
from keywin.send_input import send_mouse_events, send_mouse_flag


def send_events(*inputs: MouseEvent) -> bool:
    """
    Summary
    -------
    a low-level function to send mouse events

    Parameters
    ----------
    *inputs (tuple[x, y, mouseData, dwFlags]) : mouse event(s)

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
    return send_mouse_events(((MouseCode.MOUSE_XBUTTON1_CLICK, 0, 0, MouseCode.XBUTTON1),))


def xbutton2_click() -> bool:
    """
    Summary
    -------
    return click `xbutton2`

    Return
    --------
    success (bool) : the success of the event
    """
    return send_mouse_events(((MouseCode.MOUSE_XBUTTON2_CLICK, 0, 0, MouseCode.XBUTTON2),))


def left_press() -> bool:
    """
    Summary
    -------
    hold the left mouse button

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
    hold the right mouse button

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
    hold the middle mouse button

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
    hold `xbutton1`

    Return
    --------
    success (bool) : the success of the event
    """
    return send_mouse_events(((MouseCode.MOUSEEVENTF_XDOWN, 0, 0, MouseCode.XBUTTON1),))


def xbutton1_release() -> bool:
    """
    Summary
    -------
    release `xbutton1`

    Return
    --------
    success (bool) : the success of the event
    """
    return send_mouse_events(((MouseCode.XBUTTON1, MouseCode.MOUSEEVENTF_XUP, 0, 0),))


def xbutton2_press() -> bool:
    """
    Summary
    -------
    hold `xbutton2`

    Return
    --------
    success (bool) : the success of the event
    """
    return send_mouse_events(((MouseCode.MOUSEEVENTF_XDOWN, 0, 0, MouseCode.XBUTTON2),))


def xbutton2_release() -> bool:
    """
    Summary
    -------
    release `xbutton2`

    Return
    --------
    success (bool) : the success of the event
    """
    return send_mouse_events(((MouseCode.MOUSEEVENTF_XUP, 0, 0, MouseCode.XBUTTON2),))


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
    return send_mouse_events(((MouseCode.MOUSEEVENTF_MOVE, x, y, 0),))


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
    return send_mouse_events(((MouseCode.MOUSE_MOVE_ABSOLUTE, x, y, 0),))


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
    return send_mouse_events(((MouseCode.MOUSEEVENTF_WHEEL, 0, 0, scroll_delta),))


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
    return send_mouse_events(((MouseCode.MOUSEEVENTF_HWHEEL, 0, 0, scroll_delta),))
