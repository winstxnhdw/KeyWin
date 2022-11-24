from keywin.mouse_codes import MouseCodes
from keywin.send_input import send_mouse_event


class Mouse:

    def create_event(flags: int, x: int=0, y: int=0, mouse_data: int=0) -> list[int]:

        return [x, y, mouse_data, flags]


    def send_events(*inputs: list[int]):

        send_mouse_event(inputs)


    def click(flags: int):

        Mouse.send_events([0, 0, 0, flags])
        

    def left_click():

        Mouse.click(MouseCodes.MOUSEEVENTF_LEFTDOWN | MouseCodes.MOUSEEVENTF_LEFTUP)


    def right_click():

        Mouse.click(MouseCodes.MOUSEEVENTF_RIGHTDOWN | MouseCodes.MOUSEEVENTF_RIGHTUP)


    def middle_click():

        Mouse.click(MouseCodes.MOUSEEVENTF_MIDDLEDOWN | MouseCodes.MOUSEEVENTF_MIDDLEUP)


    def move_relative(x: int, y: int, flag: int=0):

        Mouse.send_events([x, y, 0, MouseCodes.MOUSEEVENTF_MOVE | flag])


    def move(x: int, y: int):

        Mouse.move_relative(x, y, MouseCodes.MOUSEEVENTF_ABSOLUTE)


    def scroll(scroll_delta: int, flags: int=MouseCodes.MOUSEEVENTF_WHEEL):

        Mouse.send_events([0, 0, scroll_delta, flags])


    def scroll_horizontal(scroll_delta: int):

        Mouse.scroll(scroll_delta, MouseCodes.MOUSEEVENTF_HWHEEL)