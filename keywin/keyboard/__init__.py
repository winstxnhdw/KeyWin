from keywin.send_input import send_keyboard_events
from keywin.send_input import send_unicode_events as write

__all__ = ['press', 'write']


def press(*keys: int) -> bool:
    """
    Summary
    -------
    low-level function to press a key

    Parameters
    ----------
    *keys (int) : Microsoft's [Virtual-Key Codes](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)

    Returns
    -------
    success (bool) : the success of the event
    """
    return send_keyboard_events(keys)
