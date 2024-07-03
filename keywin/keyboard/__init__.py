from keywin.send_input import press_keyboard


def press(*keys: int) -> bool:
    """
    Summary
    -------
    low-level function to press a key

    Parameters
    ----------
    *keys (int) : key code(s)

    Returns
    -------
    success (bool) : the success of the event
    """
    return press_keyboard(keys)
