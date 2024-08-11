from __future__ import annotations

from sys import platform
from typing import TypedDict

from setuptools import Extension


class Build(TypedDict):
    """
    Summary
    -------
    a typed dictionary for the build

    Attributes
    ----------
    ext_modules (list[Extension]) : a list of extensions
    """

    ext_modules: list[Extension]


def pdm_build_initialize(_):
    """
    Summary
    -------
    initialise the build
    """
    if platform in ('win32', 'cygwin', 'cli'):
        return

    raise RuntimeError('keywin only supports Windows!')


def pdm_build_update_setup_kwargs(_, kwargs: Build):
    """
    Summary
    -------
    update the setup kwargs with the extension modules
    """
    kwargs.update(
        ext_modules=[Extension('keywin.send_input', ['keywin/send_input/send_input.c'], libraries=['user32'])]
    )
