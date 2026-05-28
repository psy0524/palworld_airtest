# -*- encoding=utf8 -*-
from airtest.core.api import *

from images import IMG_BUILD_MODE_WINDOW
from input_utils import press_game_key


BUILD_MODE_OPEN = False


def open_build_mode():
    """
    건축 모드를 연다.
    실제 화면에서 이미 열려 있으면 B를 다시 누르지 않는다.
    """

    global BUILD_MODE_OPEN

    if exists(IMG_BUILD_MODE_WINDOW):
        BUILD_MODE_OPEN = True
        print("이미 건축 모드가 열려 있음")
        return

    press_game_key("B", hold=0.1, after_sleep=1.5)

    assert_exists(
        IMG_BUILD_MODE_WINDOW,
        "건축 모드 창이 표시되어야 한다."
    )

    BUILD_MODE_OPEN = True
    print("건축 모드 열기 완료")


def close_build_mode():
    """
    건축 모드를 닫는다.
    """

    global BUILD_MODE_OPEN

    if not exists(IMG_BUILD_MODE_WINDOW):
        BUILD_MODE_OPEN = False
        print("이미 건축 모드가 닫혀 있음")
        return

    press_game_key("ESC", hold=0.1, after_sleep=1)

    assert_not_exists(
        IMG_BUILD_MODE_WINDOW,
        "건축 모드 창이 닫혀야 한다."
    )

    BUILD_MODE_OPEN = False
    print("건축 모드 닫기 완료")


def recover_to_default_state():
    """
    실패했을 때만 사용하는 복구 함수.
    정상 케이스 종료 후에는 호출하지 않는다.
    """

    global BUILD_MODE_OPEN

    try:
        if exists(IMG_BUILD_MODE_WINDOW) or BUILD_MODE_OPEN:
            press_game_key("ESC", hold=0.1, after_sleep=1)
            BUILD_MODE_OPEN = False
            print("복구: 건축 모드 닫기 완료")
        else:
            BUILD_MODE_OPEN = False
            print("복구 필요 없음")

    except Exception as e:
        print(f"복구 중 예외 발생: {e}")


def click_tab(tab_image, representative_image, tab_name):
    """
    탭 클릭 후 해당 탭의 대표 항목이 표시되는지 확인한다.
    현재 통과한 방식 그대로 이미지 인식 클릭 사용.
    """

    touch(tab_image)
    sleep(1)

    if exists(representative_image):
        print(f"{tab_name} 탭 대표 항목 인식 성공")
        return

    snapshot(msg=f"{tab_name}_tab_click_failed")

    raise AssertionError(
        f"{tab_name} 탭 클릭 후 대표 항목을 찾지 못했습니다. "
        f"탭 이미지 또는 대표 항목 이미지를 다시 확인하세요."
    )