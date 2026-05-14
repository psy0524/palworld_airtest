# -*- encoding=utf8 -*-
__author__ = "qewff"

from airtest.core.api import *

# 탭 파일 import
from tab_production import test_production_tab


auto_setup(__file__, logdir=True)

connect_device("Windows:///")


def press_game_key(key, hold=0.1):
    """
    PC 게임용 키 입력 함수.
    """
    win = device()
    win.key_press(key)
    sleep(hold)
    win.key_release(key)


def open_build_mode():
    """
    Palworld 건축 모드를 연다.
    현재 기준: B 키로 건축 모드 진입.
    """
    press_game_key("B")
    sleep(1)

    snapshot(msg="건축 모드 진입 완료")


def main():
    """
    메인 실행 흐름.
    1. 건축 모드 열기
    2. 생산 탭 테스트 실행
    """

    open_build_mode()
    test_production_tab()


# =========================
# 메인 실행부
# =========================

main()