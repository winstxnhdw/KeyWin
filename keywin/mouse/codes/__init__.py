class MouseCodes:
    """
    Summary
    -------
    pre-mapped mouse codes based on [MOUSEINPUT](https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-mouseinput)
    """
    XBUTTON1                    = 0x0001
    XBUTTON2                    = 0x0002
    MOUSEEVENTF_MOVE            = 0x0001
    MOUSEEVENTF_LEFTDOWN        = 0x0002
    MOUSEEVENTF_LEFTUP          = 0x0004
    MOUSEEVENTF_RIGHTDOWN       = 0x0008
    MOUSEEVENTF_RIGHTUP         = 0x0010
    MOUSEEVENTF_MIDDLEDOWN      = 0x0020
    MOUSEEVENTF_MIDDLEUP        = 0x0040
    MOUSEEVENTF_XDOWN           = 0x0080
    MOUSEEVENTF_XUP             = 0x0100
    MOUSEEVENTF_WHEEL           = 0x0800
    MOUSEEVENTF_HWHEEL          = 0x01000
    MOUSEEVENTF_MOVE_NOCOALESCE = 0x2000
    MOUSEEVENTF_VIRTUALDESK     = 0x4000
    MOUSEEVENTF_ABSOLUTE        = 0x8000
