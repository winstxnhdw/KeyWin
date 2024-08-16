class KeyFlag:
    """
    Summary
    -------
    a class for holding the key flags
    """

    KEYEVENTF_EXTENDEDKEY = 0x01
    KEYEVENTF_KEYUP = 0x02
    KEYEVENTF_UNICODE = 0x04
    KEYEVENTF_SCANCODE = 0x08
    KEYUP_UNICODE = KEYEVENTF_KEYUP | KEYEVENTF_UNICODE
