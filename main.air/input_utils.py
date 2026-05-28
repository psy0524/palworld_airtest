# -*- encoding=utf8 -*-
from airtest.core.api import *


def press_game_key(key, hold=0.1, after_sleep=0.5):
    """
    Palworld PC 게임용 키 입력 함수.
    AirTest Windows device의 key_press/key_release 사용.
    """

    key_map = {
        "ESC": "ESCAPE",
        "ESCAPE": "ESCAPE",
        "TAB": "TAB",
        "CTRL": "CONTROL",
        "LCtrl": "LCONTROL",
        "LCTRL": "LCONTROL",
        "SHIFT": "SHIFT",
        "SPACE": "SPACE",
        "ENTER": "ENTER",
        "B": "B",
        "F": "F",
        "ALT": "MENU",
    }

    converted_key = key_map.get(key, key)

    win = device()
    win.key_press(converted_key)
    sleep(hold)
    win.key_release(converted_key)
    sleep(after_sleep)