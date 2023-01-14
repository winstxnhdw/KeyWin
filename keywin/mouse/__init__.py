from keywin.mouse.codes import MouseCodes
from keywin.send_input import send_mouse_event


def create_event(flags: int, x: int=0, y: int=0, mouse_data: int=0) -> list[int]:
    """
    Summary
    -------
    Helper function to create a mouse event

    Parameters
    ----------
    flags (int) : flag to use for the mouse event
    x (int?) : generic x-axis value
    y (int?) : generic y-axis value
    mouse_data (int?) : data to use for the mouse event
    """
    return [x, y, mouse_data, flags]


def send_events(*inputs: list[int]):
    """
    Summary
    -------
    Low-level function to send mouse events

    Parameters
    ----------
    *inputs (list[int]) : mouse event(s)
    """
    send_mouse_event(inputs)


def click(flags: int, mouse_data: int=0):
    """
    Summary
    -------
    Generic click function

    Parameters
    ----------
    flags (int) : flag to use for the mouse event
    mouse_data (int?) : data to use for the mouse event
    """
    send_events([0, 0, mouse_data, flags])


def left_click():
    """
    Summary
    -------
    Click the left mouse button
    """
    click(MouseCodes.MOUSEEVENTF_LEFTDOWN | MouseCodes.MOUSEEVENTF_LEFTUP)


def right_click():
    """
    Summary
    -------
    Click the right mouse button
    """
    click(MouseCodes.MOUSEEVENTF_RIGHTDOWN | MouseCodes.MOUSEEVENTF_RIGHTUP)


def middle_click():
    """
    Summary
    -------
    Click the middle mouse button
    """
    click(MouseCodes.MOUSEEVENTF_MIDDLEDOWN | MouseCodes.MOUSEEVENTF_MIDDLEUP)


def xbutton1_click():
    """
    Summary
    -------
    Click `xbutton1`
    """
    click(MouseCodes.MOUSEEVENTF_XDOWN | MouseCodes.MOUSEEVENTF_XUP, MouseCodes.XBUTTON1)


def xbutton2_click():
    """
    Summary
    -------
    Click `xbutton2`
    """
    click(MouseCodes.MOUSEEVENTF_XDOWN | MouseCodes.MOUSEEVENTF_XUP, MouseCodes.XBUTTON2)


def left_press():
    """
    Summary
    -------
    Press the left mouse button
    """
    click(MouseCodes.MOUSEEVENTF_LEFTDOWN)


def left_release():
    """
    Summary
    -------
    Release the left mouse button
    """
    click(MouseCodes.MOUSEEVENTF_LEFTUP)

def right_press():
    """
    Summary
    -------
    Press the right mouse button
    """
    click(MouseCodes.MOUSEEVENTF_RIGHTDOWN)


def right_release():
    """
    Summary
    -------
    Release the right mouse button
    """
    click(MouseCodes.MOUSEEVENTF_RIGHTUP)


def middle_press():
    """
    Summary
    -------
    Press the middle mouse button
    """
    click(MouseCodes.MOUSEEVENTF_MIDDLEDOWN)


def middle_release():
    """
    Summary
    -------
    Release the middle mouse button
    """
    click(MouseCodes.MOUSEEVENTF_MIDDLEUP)


def xbutton1_press():
    """
    Summary
    -------
    Press `xbutton1`
    """
    click(MouseCodes.MOUSEEVENTF_XDOWN, MouseCodes.XBUTTON1)


def xbutton1_release():
    """
    Summary
    -------
    Release `xbutton1`
    """
    click(MouseCodes.MOUSEEVENTF_XUP, MouseCodes.XBUTTON1)


def xbutton2_press():
    """
    Summary
    -------
    Press `xbutton2`
    """
    click(MouseCodes.MOUSEEVENTF_XDOWN, MouseCodes.XBUTTON2)


def xbutton2_release():
    """
    Summary
    -------
    Release `xbutton2`
    """
    click(MouseCodes.MOUSEEVENTF_XUP, MouseCodes.XBUTTON2)


def move_relative(x: int, y: int, flag: int=0):
    """
    Summary
    -------
    Move mouse relative to the current position

    Parameters
    ----------
    x (int) : amount of pixels to move the mouse on the x-axis
    y (int) : amount of pixels to move the mouse on the y-axis
    flag (int?) : flag to use for the mouse event
    """
    send_events([x, y, 0, MouseCodes.MOUSEEVENTF_MOVE | flag])


def move(x: int, y: int):
    """
    Summary
    -------
    Move mouse to an absolute position

    Parameters
    ----------
    x (int) : coordinate on the x-axis to move the mouse to
    y (int) : coordinate on the y-axis to move the mouse to
    """
    move_relative(x, y, MouseCodes.MOUSEEVENTF_ABSOLUTE)


def scroll(scroll_delta: int, flags: int=MouseCodes.MOUSEEVENTF_WHEEL):
    """
    Summary
    -------
    Scroll the vertical mouse wheel

    Parameters
    ----------
    scroll_delta (int) : amount to scroll the mouse wheel
    flag (int?) : flag to use for the mouse event
    """
    send_events([0, 0, scroll_delta, flags])


def scroll_horizontal(scroll_delta: int):
    """
    Summary
    -------
    Scroll the horizontal mouse wheel

    Parameters
    ----------
    scroll_delta (int) : amount to scroll the mouse wheel
    """
    scroll(scroll_delta, MouseCodes.MOUSEEVENTF_HWHEEL)
