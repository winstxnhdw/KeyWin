from setuptools import Extension, setup


setup(
    ext_modules=[
        Extension(
            'keywin.send_input',
            ['keywin/send_input/send_input.c'],
            libraries=['user32']
        )
    ]
)
