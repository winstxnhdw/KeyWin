from keywin.send_input import press_keyboard


def press(*keys: int):
    """
    Summary
    -------
    Low-level function to press a key

    Parameters
    ----------
    *keys (int) : key code(s)
    """
    press_keyboard(keys)
