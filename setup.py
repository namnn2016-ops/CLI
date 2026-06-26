from setuptools import setup

setup(
    name="gpt",
    version="1.0.0",
    py_modules=["main"],
    install_requires=[
        "typer",
    ],
    entry_points={
        "console_scripts": [
            "gpt=main:app",
        ],
    },
)