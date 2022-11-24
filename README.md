# KeyWin

`KeyWin` is a fast Python wrapper for Win32's SendInput function using C extensions. It is designed to be used in applications that require low-latency inputs.

## Installation

```bash
pip install git+https://github.com/winstxnhdw/KeyWin
```

## Usage

```python
from keywin import KeyCodes
from keywin import Keyboard, Mouse


def main():
    
    # Win + D
    Keyboard.press(KeyCodes.VK_LWIN, KeyCodes.VK_D)

    # Left + Right click at (100, 100)
    left_click_flag = KeyCodes.MOUSEEVENTF_LEFTDOWN | KeyCodes.MOUSEEVENTF_LEFTUP
    left_click_event = Mouse.create_event(left_click_flag, 100, 100)
    right_click_flag = KeyCodes.MOUSEEVENTF_RIGHTDOWN | KeyCodes.MOUSEEVENTF_RIGHTUP
    right_click_event = Mouse.create_event(right_click_flag, 100, 100)
    Mouse.send_events(left_click_event, right_click_event)


if __name__ == '__main__':
    main() 
```
