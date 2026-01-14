# ruff: noqa: S101

from keywin import KeyCode
from keywin.keyboard import hold, hold_unicode, press, release, release_unicode, send_events, write
from keywin.keyboard.helpers import KeyboardEvent


def test_keyboard_event() -> None:
    """
    Summary
    -------
    test the `KeyboardEvent` NamedTuple
    """
    assert send_events(
        KeyboardEvent(KeyCode.VK_A, 0, 0),
        KeyboardEvent(KeyCode.VK_B, 0, 0),
    )


def test_press() -> None:
    """
    Summary
    -------
    test the `press` function
    """
    for key in KeyCode.__dict__.values():
        if not isinstance(key, int):
            continue

        try:
            assert press(key)

        except KeyboardInterrupt:
            continue


def test_write() -> None:
    """
    Summary
    -------
    test the `write` function
    """
    assert write("Hello, world!")


def test_keyboard_helpers() -> None:
    """
    Summary
    -------
    test the keyboard helper functions
    """
    assert hold(KeyCode.VK_A)
    assert release(KeyCode.VK_A)
    assert hold_unicode(ord("A"))
    assert release_unicode(ord("A"))
