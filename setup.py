from curses import window
import os
from setuptools import setup
import py2exe

setup(
    name = "PizzaSoft Media Converter",
    version = "22.0.1",
    description="A software to convert media files to increase compatibility with different devices, editing softwares, and platforms.",
    author="PizzaSoft",
    author_email="",
    url="",
    windows=[{"script": "main.py", "icon_resources": [(1, "assets/icon.ico")]}],
    download_url = "",
    icon = "assets/icon.ico",
)
os.system("delete .\\dist\\PSMediaConverter.exe")
os.system("rename .\\dist\\main.exe PSMediaConverter.exe")
