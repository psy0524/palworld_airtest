# -*- encoding=utf8 -*-
from airtest.core.api import *

import build_common
from build_common import open_build_mode, click_tab
from input_utils import press_game_key
from images import (
    IMG_TAB_PRODUCTION,
    IMG_REP_PRODUCTION,
    IMG_ITEM_PRIMITIVE_WORKBENCH,
    IMG_BUILD_PREVIEW_UI,
)


def select_build_item(item_image, item_name):
    """
    건축물 아이콘을 이미지 인식으로 클릭한다.
    """
    touch(item_image)
    sleep(1)

    print(f"{item_name} 아이콘 클릭 완료")


def check_build_preview():
    """
    건축 프리뷰 UI가 표시되는지 확인한다.
    """
    assert_exists(
        IMG_BUILD_PREVIEW_UI,
        "건축 프리뷰 UI가 표시되어야 한다."
    )

    print("건축 프리뷰 UI 확인 완료")


def cancel_preview():
    """
    프리뷰 상태를 ESC로 취소한다.
    """
    press_game_key("ESC", hold=0.1, after_sleep=1)

    if exists(build_common.IMG_BUILD_MODE_WINDOW):
        build_common.BUILD_MODE_OPEN = True
        print("프리뷰 취소 후 건축 모드 화면 유지")
    else:
        build_common.BUILD_MODE_OPEN = False
        print("프리뷰 취소 후 건축 모드 화면 미확인")


def tc_015_primitive_workbench_preview():
    """
    PW-BLD-015 원시적인 작업대 프리뷰 확인
    """
    open_build_mode()
    click_tab(IMG_TAB_PRODUCTION, IMG_REP_PRODUCTION, "생산")
    select_build_item(IMG_ITEM_PRIMITIVE_WORKBENCH, "원시적인 작업대")
    check_build_preview()
    cancel_preview()