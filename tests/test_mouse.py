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
    send_events,
    xbutton1_click,
    xbutton1_press,
    xbutton1_release,
    xbutton2_click,
    xbutton2_press,
    xbutton2_release,
)
from keywin.mouse.helpers import MouseEvent
from keywin.mouse.mouse_code import MouseCode


def test_mouse_event():
    """
    Summary
    -------
    test the `MouseEvent` NamedTuple
    """
    assert send_events(
        MouseEvent(MouseCode.MOUSE_LEFT_CLICK, 100, 100, 0),
        MouseEvent(MouseCode.MOUSEEVENTF_WHEEL, 0, 0, 5),
    )


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
