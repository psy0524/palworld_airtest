# -*- encoding=utf8 -*-
from airtest.core.api import *

import build_common
from images import IMG_BUILD_MODE_WINDOW
from input_utils import press_game_key
from build_common import open_build_mode, close_build_mode


def tc_001_open_build_mode():
    open_build_mode()


def tc_002_close_build_mode():
    close_build_mode()


def tc_004_duplicate_open_build_mode():
    """
    PW-BLD-004 건축모드중복진입
    """

    build_common.BUILD_MODE_OPEN = False

    press_game_key("B", hold=0.1, after_sleep=1.5)

    if not exists(IMG_BUILD_MODE_WINDOW):
        snapshot(msg="PW_BLD_004_first_B_open_failed")
        raise AssertionError("4번 케이스: 첫 번째 B 입력 후 건축 모드가 열리지 않았습니다.")

    print("4번 케이스: 첫 번째 B 입력으로 건축 모드 열림 확인")
    build_common.BUILD_MODE_OPEN = True

    press_game_key("B", hold=0.1, after_sleep=1.5)

    if exists(IMG_BUILD_MODE_WINDOW):
        print("4번 케이스: 두 번째 B 입력 후에도 건축 모드가 유지됨")
        build_common.BUILD_MODE_OPEN = True
        return

    print("4번 케이스: 두 번째 B 입력 후 건축 모드가 닫힘. 정상 토글 동작으로 판단")
    build_common.BUILD_MODE_OPEN = False
    snapshot(msg="PW_BLD_004_closed_after_second_B")