# -*- encoding=utf8 -*-
from airtest.core.api import *


# =========================================================
# 생산 탭 이미지
# None을 지우고 AirTestIDE 이미지 블록을 넣으세요.
# 활성/비활성 구분하지 않고, 생산 탭 자체를 찾는 용도입니다.
# =========================================================

PRODUCTION_TAB_IMAGE = Template(r"tpl1778769654422.png", record_pos=(-0.303, -0.222), resolution=(1920, 1080))


def click_production_tab():
    """
    생산 탭을 무조건 클릭한다.
    활성화/비활성화 상태를 구분하지 않는다.
    """

    tab_pos = exists(PRODUCTION_TAB_IMAGE)

    if not tab_pos:
        snapshot(msg="생산 탭 이미지 확인 실패")
        raise AssertionError("생산 탭 이미지를 찾지 못했습니다.")

    print("[INFO] 생산 탭을 클릭합니다.")
    touch(tab_pos)
    sleep(1)

    snapshot(msg="생산 탭 클릭 완료")


def test_production_tab():
    """
    메인 파일에서 호출할 생산 탭 테스트 함수.
    """
    click_production_tab()
    print("[PASS] 생산 탭 테스트 완료")