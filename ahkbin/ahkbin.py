# -*- coding: utf-8 -*-

import os.path


def get_dir():
    return os.path.join(os.path.dirname(__file__), "ahk")


def get_executable():
    return os.path.join(get_dir(), "AutoHotkey.exe")
