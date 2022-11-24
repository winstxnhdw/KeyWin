from keywin.keycodes import KeyCodes
from keywin.send_input import press_keyboard, send_mouse_event


class Keyboard:

    def press(*keys: int):

        press_keyboard(keys)


class Mouse:

    def create_event(flags: int, x: int=0, y: int=0, mouse_data: int=0) -> list[int]:

        return [x, y, mouse_data, flags]


    def send_events(*inputs: list[int]):

        send_mouse_event(inputs)


    def click(flags: int):

        Mouse.send_events([0, 0, 0, flags])
        

    def left_click():

        Mouse.click(KeyCodes.MOUSEEVENTF_LEFTDOWN | KeyCodes.MOUSEEVENTF_LEFTUP)


    def right_click():

        Mouse.click(KeyCodes.MOUSEEVENTF_RIGHTDOWN | KeyCodes.MOUSEEVENTF_RIGHTUP)


    def middle_click():

        Mouse.click(KeyCodes.MOUSEEVENTF_MIDDLEDOWN | KeyCodes.MOUSEEVENTF_MIDDLEUP)


    def move_relative(x: int, y: int, flag: int=0):

        Mouse.send_events([x, y, 0, KeyCodes.MOUSEEVENTF_MOVE | flag])


    def move(x: int, y: int):

        Mouse.move_relative(x, y, KeyCodes.MOUSEEVENTF_ABSOLUTE)


    def scroll(scroll_delta: int, flags: int=KeyCodes.MOUSEEVENTF_WHEEL):

        Mouse.send_events([0, 0, scroll_delta, flags])


    def scroll_horizontal(scroll_delta: int):

        Mouse.scroll(scroll_delta, KeyCodes.MOUSEEVENTF_HWHEEL)

