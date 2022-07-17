from curses import window
from setuptools import setup
import py2exe

setup(
    name = "PizzaSoft Media Converter",
    version = "22.0.1",
    description="A software to convert media files to increase compatibility with different devices, editing softwares, and platforms.",
    author="PizzaSoft",
    author_email="",
    url="",
    console=["runner.py"],
    windows=[{"script": "runner.py", "icon_resources": [(1, "assets/icon.ico")]}],
    download_url = "",
)
