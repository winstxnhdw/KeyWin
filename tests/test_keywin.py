from keywin import KeyCodes
from keywin.keyboard import convert_to_key_code


def test_convert_to_key_code():
    """
    Summary
    -------
    test the `convert_to_key_code` function
    """
    assert convert_to_key_code("a") == [KeyCodes.VK_A]
