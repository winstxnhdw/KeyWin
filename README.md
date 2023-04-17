# KeyWin

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![main.yml](https://github.com/winstxnhdw/KeyWin/actions/workflows/main.yml/badge.svg)](https://github.com/winstxnhdw/KeyWin/actions/workflows/main.yml)
[![dependabot.yml](https://github.com/winstxnhdw/KeyWin/actions/workflows/dependabot.yml/badge.svg)](https://github.com/winstxnhdw/KeyWin/actions/workflows/dependabot.yml)

`KeyWin` is a fast Python wrapper for Win32's SendInput function using C extensions. It is designed to be used in applications that require low-latency inputs.

## Installation

```bash
pip install git+https://github.com/winstxnhdw/KeyWin
```

## Usage

### Keyboard

`KeyWin` provides a low-level API for keyboard inputs based on Microsoft's [Virtual-Key Codes](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes).

#### Pre-mapped Key Codes

`KeyWin` provides a set of pre-mapped key codes for common keys. These key codes are defined [here](https://github.com/winstxnhdw/KeyWin/blob/master/keywin/key_codes/__init__.py).

```python
from keywin import KeyCodes, keyboard

# Enter
keyboard.press(KeyCodes.VK_RETURN)

# Win + D
keyboard.press(KeyCodes.VK_LWIN, KeyCodes.VK_D)
```

#### Manual Key Codes

If you are unable to find the key code you need, you can enter the hex key values manually.

```python
from keywin import keyboard

# Enter
keyboard.press(0x0D)

# Win + D
keyboard.press(0x5B, 0x44)
```

### Mouse

Similar to the keyboard, `KeyWin` provides a low-level API for mouse inputs based on Microsoft's [MOUSEINPUT](https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-mouseinput) structure.

#### Helpers

`KeyWin` provides a set of helper functions for common mouse inputs.

```python
from keywin import mouse

# Move mouse 100 down and 100 right from current position
mouse.move_relative(100, 100)

# Move mouse to (100, 100)
mouse.move(100, 100)

# Left click
mouse.left_click()

# Right click
mouse.right_click()

# Middle click
mouse.middle_click()

# xbutton1 click
mouse.xbutton1_click()

# xbutton2 click
mouse.xbutton2_click()

# Press left button
mouse.left_press()

# Press right button
mouse.right_press()

# Press middle button
mouse.middle_press()

# Press xbutton1
mouse.xbutton1_press()

# Press xbutton2
mouse.xbutton2_press()

# Release left button
mouse.left_release()

# Release right button
mouse.right_release()

# Release middle button
mouse.middle_release()

# Release xbutton1
mouse.xbutton1_release()

# Release xbutton2
mouse.xbutton2_release()

# Scroll up
mouse.scroll(10)

# Scroll down
mouse.scroll(-10)

# Scroll left
mouse.scroll_horizontal(10)

# Scroll right
mouse.scroll_horizontal(-10)
```

#### Low-level Access

Rarely, you may want to use the low-level API for low-latency inputs. `create_event()` is a helper function that returns a cacheable `MOUSEINPUT` list, which can be passed to the low-level wrapper function `send_events()`.

```python
from keywin import mouse, MouseCodes


class Bot:

    def __init__(self):

        self.left_click_event = mouse.create_event(
            MouseCodes.MOUSEEVENTF_LEFTDOWN | MouseCodes.MOUSEEVENTF_LEFTUP, 100, 100
        )

        self.right_click_event = mouse.create_event(
            MouseCodes.MOUSEEVENTF_RIGHTDOWN | MouseCodes.MOUSEEVENTF_RIGHTUP, 100, 100
        )


    def dual_click_at_100(self):

        # Left + Right click at (100, 100)
        mouse.send_events(self.left_click_event, self.right_click_event)
```

## Benchmarks

`KeyWin` is designed to be used in applications that require low-latency inputs. The following benchmarks were performed against boppreh's [keyboard](https://github.com/boppreh/keyboard) and [mouse](https://github.com/boppreh/mouse) libraries. In all cases, `KeyWin` is magnitudes faster than the other libraries.

### Keyboard Benchmark

KeyWin

```python
import cProfile as profile

from keywin import keyboard, KeyCodes


def keywin():

    keyboard.press(KeyCodes.VK_SPACE)


if __name__ == '__main__':
    profile.run('keywin()')
```

```txt
6 function calls in 0.000 seconds

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    1    0.000    0.000    0.000    0.000 keyboard.py:6(press)
    1    0.000    0.000    0.000    0.000 test.py:6(keywin)
    1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
    1    0.000    0.000    0.000    0.000 {built-in method keywin.send_input.press_keyboard}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

[keyboard](https://github.com/boppreh/keyboard)

```python
import cProfile as profile

from keyboard import press_and_release


def keyboard():

    press_and_release("space")


if __name__ == '__main__':
    profile.run('keyboard()')
```

```txt
172510 function calls (172499 primitive calls) in 0.177 seconds

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.177    0.177 <string>:1(<module>)
    1    0.000    0.000    0.000    0.000 __init__.py:102(<lambda>)
    2    0.000    0.000    0.000    0.000 __init__.py:103(<lambda>)
    2    0.000    0.000    0.000    0.000 __init__.py:106(<lambda>)
    1    0.000    0.000    0.175    0.175 __init__.py:298(key_to_scan_codes)
  121    0.000    0.000    0.175    0.001 __init__.py:317(<genexpr>)
    1    0.000    0.000    0.175    0.175 __init__.py:328(parse_hotkey)
    2    0.000    0.000    0.175    0.088 __init__.py:358(<genexpr>)
    1    0.000    0.000    0.177    0.177 __init__.py:361(send)
    2    0.000    0.000    0.000    0.000 __init__.py:384(__getattr__)
    2    0.000    0.000    0.000    0.000 __init__.py:391(__getitem__)
21209    0.015    0.000    0.022    0.000 _canonical_names.py:1233(normalize_name)
18796    0.110    0.000    0.111    0.000 _winkeyboard.py:351(get_event_names)
    1    0.028    0.028    0.175    0.175 _winkeyboard.py:383(_setup_name_tables)
    1    0.000    0.000    0.000    0.000 _winkeyboard.py:393(<listcomp>)
    1    0.000    0.000    0.000    0.000 _winkeyboard.py:394(<listcomp>)
 4400    0.003    0.000    0.004    0.000 _winkeyboard.py:411(<listcomp>)
    5    0.000    0.000    0.000    0.000 _winkeyboard.py:429(<lambda>)
12488    0.002    0.000    0.002    0.000 _winkeyboard.py:431(order_key)
  121    0.000    0.000    0.175    0.001 _winkeyboard.py:567(map_name)
    2    0.001    0.001    0.002    0.001 _winkeyboard.py:577(_send_event)
    1    0.000    0.000    0.000    0.000 _winkeyboard.py:590(press)
    1    0.000    0.000    0.001    0.001 _winkeyboard.py:593(release)
    4    0.000    0.000    0.000    0.000 enum.py:359(__call__)
    4    0.000    0.000    0.000    0.000 enum.py:678(__new__)
    2    0.000    0.000    0.000    0.000 enum.py:986(__and__)
    2    0.000    0.000    0.000    0.000 re.py:222(split)
    2    0.000    0.000    0.000    0.000 re.py:288(_compile)
    3    0.000    0.000    0.000    0.000 sre_compile.py:265(_compile_charset)
    3    0.000    0.000    0.000    0.000 sre_compile.py:292(_optimize_charset)
    3    0.000    0.000    0.000    0.000 sre_compile.py:447(_simple)
    1    0.000    0.000    0.000    0.000 sre_compile.py:456(_generate_overlap_table)
    3    0.000    0.000    0.000    0.000 sre_compile.py:477(_get_iscased)
    2    0.000    0.000    0.000    0.000 sre_compile.py:485(_get_literal_prefix)
    1    0.000    0.000    0.000    0.000 sre_compile.py:516(_get_charset_prefix)
    2    0.000    0.000    0.000    0.000 sre_compile.py:560(_compile_info)
    4    0.000    0.000    0.000    0.000 sre_compile.py:619(isstring)
    2    0.000    0.000    0.000    0.000 sre_compile.py:622(_code)
    2    0.000    0.000    0.000    0.000 sre_compile.py:783(compile)
  5/2    0.000    0.000    0.000    0.000 sre_compile.py:87(_compile)
    5    0.000    0.000    0.000    0.000 sre_parse.py:112(__init__)
   11    0.000    0.000    0.000    0.000 sre_parse.py:161(__len__)
   26    0.000    0.000    0.000    0.000 sre_parse.py:165(__getitem__)
    3    0.000    0.000    0.000    0.000 sre_parse.py:169(__setitem__)
    5    0.000    0.000    0.000    0.000 sre_parse.py:173(append)
  5/2    0.000    0.000    0.000    0.000 sre_parse.py:175(getwidth)
    2    0.000    0.000    0.000    0.000 sre_parse.py:225(__init__)
   10    0.000    0.000    0.000    0.000 sre_parse.py:234(__next)
    5    0.000    0.000    0.000    0.000 sre_parse.py:250(match)
    8    0.000    0.000    0.000    0.000 sre_parse.py:255(get)
    5    0.000    0.000    0.000    0.000 sre_parse.py:287(tell)
    4    0.000    0.000    0.000    0.000 sre_parse.py:356(_escape)
    2    0.000    0.000    0.000    0.000 sre_parse.py:436(_parse_sub)
    2    0.000    0.000    0.000    0.000 sre_parse.py:494(_parse)
    2    0.000    0.000    0.000    0.000 sre_parse.py:76(__init__)
    4    0.000    0.000    0.000    0.000 sre_parse.py:82(groups)
    2    0.000    0.000    0.000    0.000 sre_parse.py:928(fix_flags)
    2    0.000    0.000    0.000    0.000 sre_parse.py:944(parse)
    1    0.000    0.000    0.177    0.177 test.py:6(keyboard)
    2    0.000    0.000    0.000    0.000 {built-in method _sre.compile}
 2016    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
    1    0.000    0.000    0.177    0.177 {built-in method builtins.exec}
21256    0.002    0.000    0.002    0.000 {built-in method builtins.isinstance}
30886/30881    0.003    0.000    0.003    0.000 {built-in method builtins.len}
   12    0.000    0.000    0.000    0.000 {built-in method builtins.min}
    2    0.000    0.000    0.000    0.000 {built-in method builtins.ord}
    2    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
  205    0.004    0.000    0.006    0.000 {built-in method builtins.sorted}
    1    0.000    0.000    0.000    0.000 {method '__exit__' of '_thread.lock' objects}
21284    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    2    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
    3    0.000    0.000    0.000    0.000 {method 'find' of 'bytearray' objects}
21217    0.003    0.000    0.003    0.000 {method 'get' of 'dict' objects}
    3    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
18301    0.002    0.000    0.002    0.000 {method 'lower' of 'str' objects}
    2    0.000    0.000    0.000    0.000 {method 'split' of 're.Pattern' objects}
    2    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
    1    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
```

### Mouse Benchmark

KeyWin

```python
import cProfile as profile

from keywin import mouse, MouseCodes


def keywin():

    move_absolute_flag = MouseCodes.MOUSEEVENTF_MOVE | MouseCodes.MOUSEEVENTF_ABSOLUTE
    left_click_flag = MouseCodes.MOUSEEVENTF_LEFTDOWN | MouseCodes.MOUSEEVENTF_LEFTUP
    right_click_flag = MouseCodes.MOUSEEVENTF_RIGHTDOWN | MouseCodes.MOUSEEVENTF_RIGHTUP
    desired_position = (100, 100)

    # Left + Right click at (100, 100)
    mouse.send_events([
        *desired_position, 0, move_absolute_flag | left_click_flag
    ],
    [
        *desired_position, 0, move_absolute_flag | right_click_flag
    ])


if __name__ == '__main__':
    profile.run('keywin()')
```

```txt
6 function calls in 0.004 seconds

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.004    0.004 <string>:1(<module>)
    1    0.000    0.000    0.004    0.004 mouse.py:12(send_events)
    1    0.000    0.000    0.004    0.004 test.py:9(keywin)
    1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
    1    0.004    0.004    0.004    0.004 {built-in method keywin.send_input.send_mouse_event}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

[mouse](https://github.com/boppreh/mouse)

```python
import cProfile as profile

from mouse import click, move, right_click


def mouse():

    move(100, 100)
    click()
    right_click()


if __name__ == '__main__':
    profile.run('mouse()')
```

```txt
35 function calls in 0.008 seconds

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.008    0.008 <string>:1(<module>)
    1    0.000    0.000    0.001    0.001 __init__.py:101(right_click)
    1    0.000    0.000    0.000    0.000 __init__.py:109(move)
    1    0.000    0.000    0.000    0.000 __init__.py:199(get_position)
    3    0.000    0.000    0.000    0.000 __init__.py:391(__getitem__)
    2    0.000    0.000    0.008    0.004 __init__.py:91(click)
    4    0.000    0.000    0.000    0.000 _winmouse.py:179(_translate_button)
    2    0.004    0.002    0.004    0.002 _winmouse.py:185(press)
    2    0.003    0.002    0.003    0.002 _winmouse.py:190(release)
    1    0.000    0.000    0.000    0.000 _winmouse.py:199(move_to)
    1    0.000    0.000    0.000    0.000 _winmouse.py:208(get_position)
    1    0.000    0.000    0.008    0.008 test.py:6(mouse)
    1    0.000    0.000    0.000    0.000 {built-in method _ctypes.byref}
    1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
    3    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
    3    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    3    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
```

## Development

You can build locally by running `setuptools`.

```bash
python setup.py build_ext --inplace
```
