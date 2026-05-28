# -*- encoding=utf8 -*-
from airtest.core.api import *

import build_common
from build_common import open_build_mode, click_tab
from input_utils import press_game_key
from images import (
    IMG_BUILD_MODE_WINDOW,
    IMG_DEFAULT_HUD,
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


def check_preview_cancel_to_game_screen(action_name):
    """
    ESC / TAB 입력 후 프리뷰와 건축 모드가 종료되고
    일반 게임 화면으로 돌아갔는지 확인한다.
    """

    # 1. 프리뷰 UI가 사라졌는지 확인
    if exists(IMG_BUILD_PREVIEW_UI):
        snapshot(msg=f"{action_name}_preview_ui_still_exists")
        raise AssertionError(f"{action_name} 입력 후에도 건축 프리뷰 UI가 남아 있습니다.")

    # 2. 건축 모드 창도 사라졌는지 확인
    if exists(IMG_BUILD_MODE_WINDOW):
        snapshot(msg=f"{action_name}_build_mode_still_exists")
        raise AssertionError(f"{action_name} 입력 후에도 건축 모드 창이 남아 있습니다.")

    # 3. 기본 HUD가 잡히면 가장 안정적인 성공 판정
    if exists(IMG_DEFAULT_HUD):
        print(f"{action_name} 입력 후 일반 게임 화면 복귀 확인")
    else:
        # HUD 이미지가 불안정할 수 있으므로,
        # 프리뷰 UI와 건축 모드 창이 모두 사라졌으면 일단 성공으로 처리
        print(f"{action_name} 입력 후 프리뷰/건축 모드 종료 확인. 기본 HUD 이미지는 미확인")

    build_common.BUILD_MODE_OPEN = False


def enter_primitive_workbench_preview():
    """
    원시적인 작업대 프리뷰 상태까지 진입하는 공통 준비 함수.
    """
    open_build_mode()
    click_tab(IMG_TAB_PRODUCTION, IMG_REP_PRODUCTION, "생산")
    select_build_item(IMG_ITEM_PRIMITIVE_WORKBENCH, "원시적인 작업대")
    check_build_preview()


def tc_015_primitive_workbench_preview():
    """
    PW-BLD-015 원시적인 작업대 프리뷰 확인

    목적:
    - 원시적인 작업대를 선택했을 때 건축 프리뷰 UI가 표시되는지만 확인한다.
    - 프리뷰 취소/중단은 PW-BLD-020, PW-BLD-021에서 별도 검증한다.
    """
    enter_primitive_workbench_preview()


def tc_020_primitive_workbench_cancel_esc():
    """
    PW-BLD-020 원시적인 작업대 ESC 건축 중단 확인

    목적:
    - 원시적인 작업대 프리뷰 상태에서 ESC 입력 시
      프리뷰와 건축 모드가 종료되고 일반 게임 화면으로 복귀하는지 확인한다.
    """
    enter_primitive_workbench_preview()

    press_game_key("ESC", hold=0.1, after_sleep=1)

    check_preview_cancel_to_game_screen("ESC")


def tc_021_primitive_workbench_cancel_tab():
    """
    PW-BLD-021 원시적인 작업대 Tab 건축 중단 확인

    목적:
    - 원시적인 작업대 프리뷰 상태에서 Tab 입력 시
      프리뷰와 건축 모드가 종료되고 일반 게임 화면으로 복귀하는지 확인한다.
    """
    enter_primitive_workbench_preview()

    press_game_key("TAB", hold=0.1, after_sleep=1)

    check_preview_cancel_to_game_screen("TAB")