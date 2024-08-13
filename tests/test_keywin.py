from keywin import KeyCode, MouseCode
from keywin.generic import send_input
from keywin.keyboard import press, write
from keywin.mouse import (
    left_click,
    left_press,
    left_release,
    middle_click,
    middle_press,
    middle_release,
    move,
    move_relative,
    right_click,
    right_press,
    right_release,
    scroll,
    scroll_horizontal,
    xbutton1_click,
    xbutton1_press,
    xbutton1_release,
    xbutton2_click,
    xbutton2_press,
    xbutton2_release,
)


def test_send_input():
    """
    Summary
    -------
    test the `send_input` function
    """
    assert send_input(
        {'key': KeyCode.VK_LCONTROL, 'release': False},
        {'key': KeyCode.VK_LSHIFT, 'release': False},
        {'key': KeyCode.VK_ESCAPE, 'release': False},
        {'key': KeyCode.VK_LCONTROL, 'release': 2},
        {'key': KeyCode.VK_LSHIFT, 'release': 2},
        {'key': KeyCode.VK_ESCAPE, 'release': 2},
        {'x': 0, 'y': 0, 'data': 0, 'flags': MouseCode.MOUSE_MOVE_ABSOLUTE},
    )


def test_press():
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


def test_write():
    """
    Summary
    -------
    test the `write` function
    """
    assert write('Hello, world!')


def test_mouse_helpers():
    """
    Summary
    -------
    test the mouse helper functions
    """
    assert left_click()
    assert left_press()
    assert left_release()
    assert right_click()
    assert right_press()
    assert right_release()
    assert middle_click()
    assert middle_press()
    assert middle_release()
    assert xbutton1_click()
    assert xbutton1_press()
    assert xbutton1_release()
    assert xbutton2_click()
    assert xbutton2_press()
    assert xbutton2_release()
    assert scroll(0)
    assert scroll(-1)
    assert scroll_horizontal(0)
    assert scroll_horizontal(-1)
    assert move(0, 0)
    assert move_relative(0, 0)
    assert not move(0xFFFFFFFFFFFFFFFFF, 0xFFFFFFFFFFFFFFFFF)
    assert not move_relative(0xFFFFFFFFFFFFFFFFF, 0xFFFFFFFFFFFFFFFFF)
    assert not scroll(0xFFFFFFFFFFFFFFFFF)
    assert not scroll_horizontal(0xFFFFFFFFFFFFFFFFF)
