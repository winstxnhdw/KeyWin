from keywin.mouse_codes import MouseCodes
from keywin.send_input import send_mouse_event


class Mouse:

    def create_event(flags: int, x: int=0, y: int=0, mouse_data: int=0) -> list[int]:

        return [x, y, mouse_data, flags]


    def send_events(*inputs: list[int]):

        send_mouse_event(inputs)


    def click(flags: int, mouse_data: int=0):

        Mouse.send_events([0, 0, mouse_data, flags])
        

    def left_click():

        Mouse.click(MouseCodes.MOUSEEVENTF_LEFTDOWN | MouseCodes.MOUSEEVENTF_LEFTUP)


    def right_click():

        Mouse.click(MouseCodes.MOUSEEVENTF_RIGHTDOWN | MouseCodes.MOUSEEVENTF_RIGHTUP)


    def middle_click():

        Mouse.click(MouseCodes.MOUSEEVENTF_MIDDLEDOWN | MouseCodes.MOUSEEVENTF_MIDDLEUP)


    def xbutton1_click():

        Mouse.click(MouseCodes.MOUSEEVENTF_XDOWN | MouseCodes.MOUSEEVENTF_XUP, 0x0001)


    def xbutton2_click():

        Mouse.click(MouseCodes.MOUSEEVENTF_XDOWN | MouseCodes.MOUSEEVENTF_XUP, 0x0002)


    def left_press():

        Mouse.click(MouseCodes.MOUSEEVENTF_LEFTDOWN)


    def left_release():

        Mouse.click(MouseCodes.MOUSEEVENTF_LEFTUP)

    def right_press():

        Mouse.click(MouseCodes.MOUSEEVENTF_RIGHTDOWN)

    
    def right_release():
            
        Mouse.click(MouseCodes.MOUSEEVENTF_RIGHTUP)


    def middle_press():

        Mouse.click(MouseCodes.MOUSEEVENTF_MIDDLEDOWN)

    
    def middle_release():

        Mouse.click(MouseCodes.MOUSEEVENTF_MIDDLEUP)


    def xbutton1_press():

        Mouse.click(MouseCodes.MOUSEEVENTF_XDOWN, 0x0001)


    def xbutton1_release():

        Mouse.click(MouseCodes.MOUSEEVENTF_XUP, 0x0001)


    def xbutton2_press():

        Mouse.click(MouseCodes.MOUSEEVENTF_XDOWN, 0x0002)
    

    def xbutton2_release():

        Mouse.click(MouseCodes.MOUSEEVENTF_XUP, 0x0002)


    def move_relative(x: int, y: int, flag: int=0):

        Mouse.send_events([x, y, 0, MouseCodes.MOUSEEVENTF_MOVE | flag])


    def move(x: int, y: int):

        Mouse.move_relative(x, y, MouseCodes.MOUSEEVENTF_ABSOLUTE)


    def scroll(scroll_delta: int, flags: int=MouseCodes.MOUSEEVENTF_WHEEL):

        Mouse.send_events([0, 0, scroll_delta, flags])


    def scroll_horizontal(scroll_delta: int):

        Mouse.scroll(scroll_delta, MouseCodes.MOUSEEVENTF_HWHEEL)