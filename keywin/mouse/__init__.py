from keywin.mouse.codes import MouseCodes
from keywin.send_input import send_mouse_event


def create_event(flags: int, x: int = 0, y: int = 0, mouse_data: int = 0) -> list[int]:
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
    event (list[int]) : the mouse event
    """
    return [x, y, mouse_data, flags]


def send_events(*inputs: list[int]) -> bool:
    """
    Summary
    -------
    low-level function to send mouse events

    Parameters
    ----------
    *inputs (list[int]) : mouse event(s)

    Return
    --------
    success (bool) : the success of the event
    """
    return send_mouse_event(inputs)


def click(flags: int, mouse_data: int = 0) -> bool:
    """
    Summary
    -------
    generic click function

    Parameters
    ----------
    flags (int) : flag to use for the mouse event
    mouse_data (int?) : data to use for the mouse event

    Return
    --------
    success (bool) : the success of the event
    """
    return send_events([0, 0, mouse_data, flags])


def left_click() -> bool:
    """
    Summary
    -------
   return click the left mouse button

    Return
    --------
    success (bool) : the success of the event
    """
    return click(MouseCodes.MOUSEEVENTF_LEFTDOWN | MouseCodes.MOUSEEVENTF_LEFTUP)


def right_click() -> bool:
    """
    Summary
    -------
   return click the right mouse button

    Return
    --------
    success (bool) : the success of the event
    """
    return click(MouseCodes.MOUSEEVENTF_RIGHTDOWN | MouseCodes.MOUSEEVENTF_RIGHTUP)


def middle_click() -> bool:
    """
    Summary
    -------
   return click the middle mouse button

    Return
    --------
    success (bool) : the success of the event
    """
    return click(MouseCodes.MOUSEEVENTF_MIDDLEDOWN | MouseCodes.MOUSEEVENTF_MIDDLEUP)


def xbutton1_click() -> bool:
    """
    Summary
    -------
   return click `xbutton1`

    Return
    --------
    success (bool) : the success of the event
    """
    return click(MouseCodes.MOUSEEVENTF_XDOWN | MouseCodes.MOUSEEVENTF_XUP, MouseCodes.XBUTTON1)


def xbutton2_click() -> bool:
    """
    Summary
    -------
   return click `xbutton2`

    Return
    --------
    success (bool) : the success of the event
    """
    return click(MouseCodes.MOUSEEVENTF_XDOWN | MouseCodes.MOUSEEVENTF_XUP, MouseCodes.XBUTTON2)


def left_press() -> bool:
    """
    Summary
    -------
    press the left mouse button

    Return
    --------
    success (bool) : the success of the event
    """
    return click(MouseCodes.MOUSEEVENTF_LEFTDOWN)


def left_release() -> bool:
    """
    Summary
    -------
    release the left mouse button

    Return
    --------
    success (bool) : the success of the event
    """
    return click(MouseCodes.MOUSEEVENTF_LEFTUP)

def right_press() -> bool:
    """
    Summary
    -------
    press the right mouse button

    Return
    --------
    success (bool) : the success of the event
    """
    return click(MouseCodes.MOUSEEVENTF_RIGHTDOWN)


def right_release() -> bool:
    """
    Summary
    -------
    release the right mouse button

    Return
    --------
    success (bool) : the success of the event
    """
    return click(MouseCodes.MOUSEEVENTF_RIGHTUP)


def middle_press() -> bool:
    """
    Summary
    -------
    press the middle mouse button

    Return
    --------
    success (bool) : the success of the event
    """
    return click(MouseCodes.MOUSEEVENTF_MIDDLEDOWN)


def middle_release() -> bool:
    """
    Summary
    -------
    release the middle mouse button

    Return
    --------
    success (bool) : the success of the event
    """
    return click(MouseCodes.MOUSEEVENTF_MIDDLEUP)


def xbutton1_press() -> bool:
    """
    Summary
    -------
    press `xbutton1`

    Return
    --------
    success (bool) : the success of the event
    """
    return click(MouseCodes.MOUSEEVENTF_XDOWN, MouseCodes.XBUTTON1)


def xbutton1_release() -> bool:
    """
    Summary
    -------
    release `xbutton1`

    Return
    --------
    success (bool) : the success of the event
    """
    return click(MouseCodes.MOUSEEVENTF_XUP, MouseCodes.XBUTTON1)


def xbutton2_press() -> bool:
    """
    Summary
    -------
    press `xbutton2`

    Return
    --------
    success (bool) : the success of the event
    """
    return click(MouseCodes.MOUSEEVENTF_XDOWN, MouseCodes.XBUTTON2)


def xbutton2_release() -> bool:
    """
    Summary
    -------
    release `xbutton2`

    Return
    --------
    success (bool) : the success of the event
    """
    return click(MouseCodes.MOUSEEVENTF_XUP, MouseCodes.XBUTTON2)


def move_relative(x: int, y: int, flag: int = 0) -> bool:
    """
    Summary
    -------
    move mouse relative to the current position

    Parameters
    ----------
    x (int) : amount of pixels to move the mouse on the x-axis
    y (int) : amount of pixels to move the mouse on the y-axis
    flag (int?) : flag to use for the mouse event

    Return
    --------
    success (bool) : the success of the event
    """
    return send_events([x, y, 0, MouseCodes.MOUSEEVENTF_MOVE | flag])


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
    return move_relative(x, y, MouseCodes.MOUSEEVENTF_ABSOLUTE)


def scroll(scroll_delta: int, flags: int = MouseCodes.MOUSEEVENTF_WHEEL) -> bool:
    """
    Summary
    -------
    scroll the vertical mouse wheel

    Parameters
    ----------
    scroll_delta (int) : amount to scroll the mouse wheel
    flag (int?) : flag to use for the mouse event

    Return
    --------
    success (bool) : the success of the event
    """
    return send_events([0, 0, scroll_delta, flags])


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
    return scroll(scroll_delta, MouseCodes.MOUSEEVENTF_HWHEEL)
