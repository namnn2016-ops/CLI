from setuptools import setup

setup(
    name="namgpt",
    version="1.0.0",
    py_modules=["main"],
    install_requires=[
        "typer",
    ],
    entry_points={
        "console_scripts": [
            "namgpt=main:app",
        ],
    },
)