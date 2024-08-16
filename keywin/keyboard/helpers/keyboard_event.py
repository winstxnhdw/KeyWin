from typing import NamedTuple


class KeyboardEvent(NamedTuple):
    """
    Summary
    -------
    a NamedTuple based on [KEYBDINPUT](https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-keybdinput)

    Attributes
    ----------
    key (int) : the key code to press
    scan (int) : the scan code to press
    flags (int) : the flags
    """

    key: int
    scan: int
    flags: int
