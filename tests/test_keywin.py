from keywin import KeyCodes
from keywin.keyboard.utils import convert_to_key_code


def test_convert_to_key_code():
    """
    Summary
    -------
    test the `convert_to_key_code` function
    """
    assert convert_to_key_code("a") == [[KeyCodes.VK_A]]
    assert convert_to_key_code("A") == [[KeyCodes.VK_SHIFT, KeyCodes.VK_A]]
    assert convert_to_key_code("Hello!") == [
        [KeyCodes.VK_SHIFT, KeyCodes.VK_H],
        [KeyCodes.VK_E, KeyCodes.VK_L, KeyCodes.VK_L, KeyCodes.VK_O],
        [KeyCodes.VK_SHIFT, KeyCodes.VK_1],
    ]
