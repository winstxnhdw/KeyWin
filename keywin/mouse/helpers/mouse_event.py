from typing import NamedTuple


class MouseEvent(NamedTuple):
    """
    Summary
    -------
    a named tuple for the mouse event

    Attributes
    ----------
    flags (int) : Microsoft's [mouse flags](https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-mouseinput)
    x (int) : generic x-axis value
    y (int) : generic y-axis value
    mouse_data (int) : data to use for the mouse event
    """

    flags: int
    x: int = 0
    y: int = 0
    mouse_data: int = 0
