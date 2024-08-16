from keywin.keyboard.helpers import KeyboardEvent
from keywin.keyboard.key_flag import KeyFlag
from keywin.send_input import send_keyboard_events, send_keyboard_press_events
from keywin.send_input import send_unicode_events as write

__all__ = (
    'send_events',
    'press',
    'hold',
    'release',
    'write',
    'hold_unicode',
    'release_unicode',
)


def send_events(*events: KeyboardEvent) -> bool:
    """
    Summary
    -------
    a low-level wrapper to send keyboard events

    Parameters
    ----------
    *events (tuple[wVk, wScan, dwFlags]) : keyboard event(s)

    Returns
    -------
    success (bool) : the success of the event
    """
    return send_keyboard_events(events)


def press(*keys: int) -> bool:
    """
    Summary
    -------
    a low-level wrapper for pressing a key

    Parameters
    ----------
    *keys (int) : Microsoft's [Virtual-Key Codes](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)

    Returns
    -------
    success (bool) : the success of the event
    """
    return send_keyboard_press_events(keys)


def hold(*keys: int) -> bool:
    """
    Summary
    -------
    a low-level wrapper for holding a key

    Parameters
    ----------
    *keys (int) : Microsoft's [Virtual-Key Codes](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)

    Returns
    -------
    success (bool) : the success of the event
    """
    return send_keyboard_events(tuple((key, 0, 0) for key in keys))


def release(*keys: int) -> bool:
    """
    Summary
    -------
    a low-level wrapper for releasing a key

    Parameters
    ----------
    *keys (int) : Microsoft's [Virtual-Key Codes](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)

    Returns
    -------
    success (bool) : the success of the event
    """
    return send_keyboard_events(tuple((key, 0, KeyFlag.KEYEVENTF_KEYUP) for key in keys))


def hold_unicode(*unicodes: int) -> bool:
    """
    Summary
    -------
    a low-level wrapper for holding a unicode key

    Parameters
    ----------
    *unicodes (int) : unicode representation of a character

    Returns
    -------
    success (bool) : the success of the event
    """
    return send_keyboard_events(tuple((0, unicode, KeyFlag.KEYEVENTF_UNICODE) for unicode in unicodes))


def release_unicode(*unicodes: int) -> bool:
    """
    Summary
    -------
    a low-level wrapper for releasing a unicode key

    Parameters
    ----------
    *unicodes (int) : unicode representation of a character

    Returns
    -------
    success (bool) : the success of the event
    """
    return send_keyboard_events(tuple((0, unicode, KeyFlag.KEYUP_UNICODE) for unicode in unicodes))
