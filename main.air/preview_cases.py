# -*- encoding=utf8 -*-
from airtest.core.api import *

import build_common
from build_common import open_build_mode, click_tab
from input_utils import press_game_key
from images import (
    IMG_BUILD_MODE_WINDOW,
    IMG_DEFAULT_HUD,
    IMG_BUILD_PREVIEW_UI,

    IMG_TAB_PRODUCTION,
    IMG_TAB_PAL,
    IMG_TAB_STORAGE,
    IMG_TAB_FOOD,
    IMG_TAB_INFRA,
    IMG_TAB_LIGHTING,
    IMG_TAB_ARCHITECTURE,
    IMG_TAB_DEFENSE,
    IMG_TAB_FURNITURE,
    IMG_TAB_MISC,

    IMG_REP_PRODUCTION,
    IMG_REP_PAL,
    IMG_REP_STORAGE,
    IMG_REP_FOOD,
    IMG_REP_INFRA,
    IMG_REP_LIGHTING,
    IMG_REP_ARCHITECTURE,
    IMG_REP_DEFENSE,
    IMG_REP_FURNITURE,
    IMG_REP_MISC,

    IMG_ITEM_PRIMITIVE_WORKBENCH,
    IMG_ITEM_REPAIR_BENCH,
    IMG_ITEM_PAL_BOX,
    IMG_ITEM_WOOD_WALL_SHELF,
    IMG_ITEM_STEEL_WALL_SHELF,
    IMG_ITEM_CAMPFIRE,
    IMG_ITEM_BASIC_BED,
    IMG_ITEM_WALL_TORCH,

    IMG_ITEM_WOOD_FOUNDATION,
    IMG_ITEM_WOOD_WALL,
    IMG_ITEM_WOOD_DOOR,
    IMG_ITEM_WOOD_TRIANGLE_WALL,
    IMG_ITEM_WOOD_ROOF,
    IMG_ITEM_WOOD_SLOPED_ROOF,
    IMG_ITEM_WOOD_CORNER_ROOF,
    IMG_ITEM_WOOD_PYRAMID_ROOF,
    IMG_ITEM_WOOD_STAIRS,
    IMG_ITEM_LADDER,

    IMG_ITEM_ALARM_BELL,

    IMG_ITEM_SQUARE_TABLE,
    IMG_ITEM_WOOD_CHAIR,
    IMG_ITEM_ANTIQUE_RED_CARPET,
    IMG_ITEM_WOOD_WALL_DECOR_SHELF,
    IMG_ITEM_HOUSEPLANT,

    IMG_ITEM_SIGNBOARD,
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


def enter_building_preview(tab_image, representative_image, tab_name, item_image, item_name, scroll_down=False):
    """
    특정 탭에서 특정 건축물 프리뷰 상태까지 진입한다.
    """
    open_build_mode()
    click_tab(tab_image, representative_image, tab_name)

    if scroll_down:
        win = device()
        win.mouse_move((1545, 315))
        sleep(0.2)
        win.mouse_down()
        sleep(0.2)
        win.mouse_move((1545, 730))
        sleep(0.5)
        win.mouse_up()
        sleep(0.5)

    select_build_item(item_image, item_name)
    check_build_preview()


def cleanup_after_preview():
    """
    프리뷰 진입 확인 케이스 후 다음 케이스를 위한 상태 정리.
    이 동작은 검증 목적이 아니라 자동화 안정화를 위한 후처리다.
    ESC/TAB 취소 검증은 별도 케이스에서 수행한다.
    """
    press_game_key("ESC", hold=0.1, after_sleep=1)

    if exists(IMG_BUILD_MODE_WINDOW):
        build_common.BUILD_MODE_OPEN = True
        print("후처리: 건축 모드 화면 유지")
    else:
        build_common.BUILD_MODE_OPEN = False
        print("후처리: 일반 게임 화면 복귀 또는 건축 모드 종료")


def check_cancel_to_game_screen(action_name):
    """
    ESC / TAB 입력 후 프리뷰와 건축 모드가 종료되고
    일반 게임 화면으로 돌아갔는지 확인한다.
    """

    if exists(IMG_BUILD_PREVIEW_UI):
        snapshot(msg=f"{action_name}_preview_ui_still_exists")
        raise AssertionError(f"{action_name} 입력 후에도 건축 프리뷰 UI가 남아 있습니다.")

    if exists(IMG_BUILD_MODE_WINDOW):
        snapshot(msg=f"{action_name}_build_mode_still_exists")
        raise AssertionError(f"{action_name} 입력 후에도 건축 모드 창이 남아 있습니다.")

    if exists(IMG_DEFAULT_HUD):
        print(f"{action_name} 입력 후 일반 게임 화면 복귀 확인")
    else:
        print(f"{action_name} 입력 후 프리뷰/건축 모드 종료 확인. 기본 HUD 이미지는 미확인")

    build_common.BUILD_MODE_OPEN = False


def make_preview_case(tab_image, representative_image, tab_name, item_image, item_name, scroll_down=False):
    """
    건축물 프리뷰 진입 확인 케이스 생성.
    """
    def _case():
        enter_building_preview(
            tab_image,
            representative_image,
            tab_name,
            item_image,
            item_name,
            scroll_down
        )
        cleanup_after_preview()

    return _case


def make_cancel_case(tab_image, representative_image, tab_name, item_image, item_name, cancel_key, scroll_down=False):
    """
    건축물 프리뷰 상태에서 ESC 또는 TAB으로 취소하는 케이스 생성.
    """
    def _case():
        enter_building_preview(
            tab_image,
            representative_image,
            tab_name,
            item_image,
            item_name,
            scroll_down
        )

        press_game_key(cancel_key, hold=0.1, after_sleep=1)

        check_cancel_to_game_screen(cancel_key)

    return _case


# ---------------------------------------------------------
# 프리뷰 자동화 대상 건축물 목록
# ---------------------------------------------------------

BUILDING_PREVIEW_TARGETS = [
    {
        "item_name": "원시적인 작업대",
        "tab_name": "생산",
        "tab_image": IMG_TAB_PRODUCTION,
        "representative_image": IMG_REP_PRODUCTION,
        "item_image": IMG_ITEM_PRIMITIVE_WORKBENCH,
        "preview": ("PW-BLD-015", "원시적인 작업대 프리뷰 확인"),
        "esc": ("PW-BLD-020", "원시적인 작업대 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-021", "원시적인 작업대 Tab 건축 중단 확인"),
    },
    {
        "item_name": "수리대",
        "tab_name": "생산",
        "tab_image": IMG_TAB_PRODUCTION,
        "representative_image": IMG_REP_PRODUCTION,
        "item_image": IMG_ITEM_REPAIR_BENCH,
        "preview": ("PW-BLD-022", "수리대 프리뷰"),
        "esc": ("PW-BLD-027", "수리대 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-028", "수리대 Tab 건축 중단 확인"),
    },
    {
        "item_name": "팰 상자",
        "tab_name": "팰",
        "tab_image": IMG_TAB_PAL,
        "representative_image": IMG_REP_PAL,
        "item_image": IMG_ITEM_PAL_BOX,
        "preview": ("PW-BLD-029", "팰 상자 설치가능 1개 프리뷰"),
        "esc": ("PW-BLD-034", "팰 상자 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-035", "팰 상자 Tab 건축 중단 확인"),
    },
    {
        "item_name": "나무 벽걸이 선반",
        "tab_name": "수납",
        "tab_image": IMG_TAB_STORAGE,
        "representative_image": IMG_REP_STORAGE,
        "item_image": IMG_ITEM_WOOD_WALL_SHELF,
        "preview": ("PW-BLD-038", "나무 벽걸이 선반 프리뷰"),
        "esc": ("PW-BLD-043", "나무 벽걸이 선반 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-044", "나무 벽걸이 선반 Tab 건축 중단 확인"),
    },
    {
        "item_name": "강철 벽걸이 선반",
        "tab_name": "수납",
        "tab_image": IMG_TAB_STORAGE,
        "representative_image": IMG_REP_STORAGE,
        "item_image": IMG_ITEM_STEEL_WALL_SHELF,
        "preview": ("PW-BLD-045", "강철 벽걸이 선반 프리뷰"),
        "esc": ("PW-BLD-050", "강철 벽걸이 선반 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-051", "강철 벽걸이 선반 Tab 건축 중단 확인"),
    },
    {
        "item_name": "모닥불",
        "tab_name": "식료품",
        "tab_image": IMG_TAB_FOOD,
        "representative_image": IMG_REP_FOOD,
        "item_image": IMG_ITEM_CAMPFIRE,
        "preview": ("PW-BLD-056", "모닥불 프리뷰"),
        "esc": ("PW-BLD-061", "모닥불 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-062", "모닥불 Tab 건축 중단 확인"),
    },
    {
        "item_name": "하급 침대",
        "tab_name": "인프라",
        "tab_image": IMG_TAB_INFRA,
        "representative_image": IMG_REP_INFRA,
        "item_image": IMG_ITEM_BASIC_BED,
        "preview": ("PW-BLD-063", "하급 침대 프리뷰"),
        "esc": ("PW-BLD-068", "하급 침대 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-069", "하급 침대 Tab 건축 중단 확인"),
    },
    {
        "item_name": "벽걸이 횃불",
        "tab_name": "조명",
        "tab_image": IMG_TAB_LIGHTING,
        "representative_image": IMG_REP_LIGHTING,
        "item_image": IMG_ITEM_WALL_TORCH,
        "preview": ("PW-BLD-070", "벽걸이 횃불 프리뷰"),
        "esc": ("PW-BLD-075", "벽걸이 횃불 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-076", "벽걸이 횃불 Tab 건축 중단 확인"),
    },

    {
        "item_name": "나무 피라미드 지붕",
        "tab_name": "건축",
        "tab_image": IMG_TAB_ARCHITECTURE,
        "representative_image": IMG_REP_ARCHITECTURE,
        "item_image": IMG_ITEM_WOOD_PYRAMID_ROOF,
        "preview": ("PW-BLD-079", "나무 피라미드 지붕 프리뷰"),
        "esc": ("PW-BLD-085", "나무 피라미드 지붕 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-086", "나무 피라미드 지붕 Tab 건축 중단 확인"),
    },
    {
        "item_name": "나무 모서리 지붕",
        "tab_name": "건축",
        "tab_image": IMG_TAB_ARCHITECTURE,
        "representative_image": IMG_REP_ARCHITECTURE,
        "item_image": IMG_ITEM_WOOD_CORNER_ROOF,
        "preview": ("PW-BLD-087", "나무 모서리 지붕 프리뷰"),
        "esc": ("PW-BLD-093", "나무 모서리 지붕 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-094", "나무 모서리 지붕 Tab 건축 중단 확인"),
    },
    {
        "item_name": "나무 경사 지붕",
        "tab_name": "건축",
        "tab_image": IMG_TAB_ARCHITECTURE,
        "representative_image": IMG_REP_ARCHITECTURE,
        "item_image": IMG_ITEM_WOOD_SLOPED_ROOF,
        "preview": ("PW-BLD-095", "나무 경사 지붕 프리뷰"),
        "esc": ("PW-BLD-101", "나무 경사 지붕 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-102", "나무 경사 지붕 Tab 건축 중단 확인"),
    },
    {
        "item_name": "나무 삼각 벽",
        "tab_name": "건축",
        "tab_image": IMG_TAB_ARCHITECTURE,
        "representative_image": IMG_REP_ARCHITECTURE,
        "item_image": IMG_ITEM_WOOD_TRIANGLE_WALL,
        "preview": ("PW-BLD-103", "나무 삼각 벽 프리뷰"),
        "esc": ("PW-BLD-108", "나무 삼각 벽 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-109", "나무 삼각 벽 Tab 건축 중단 확인"),
    },
    {
        "item_name": "나무 토대",
        "tab_name": "건축",
        "tab_image": IMG_TAB_ARCHITECTURE,
        "representative_image": IMG_REP_ARCHITECTURE,
        "item_image": IMG_ITEM_WOOD_FOUNDATION,
        "preview": ("PW-BLD-117", "나무토대프리뷰"),
        "esc": ("PW-BLD-115", "나무 토대 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-116", "나무 토대 Tab 건축 중단 확인"),
    },
    {
        "item_name": "나무 지붕",
        "tab_name": "건축",
        "tab_image": IMG_TAB_ARCHITECTURE,
        "representative_image": IMG_REP_ARCHITECTURE,
        "item_image": IMG_ITEM_WOOD_ROOF,
        "preview": ("PW-BLD-118", "나무 지붕 프리뷰"),
        "esc": ("PW-BLD-124", "나무 지붕 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-125", "나무 지붕 Tab 건축 중단 확인"),
    },
    {
        "item_name": "나무 계단",
        "tab_name": "건축",
        "tab_image": IMG_TAB_ARCHITECTURE,
        "representative_image": IMG_REP_ARCHITECTURE,
        "item_image": IMG_ITEM_WOOD_STAIRS,
        "preview": ("PW-BLD-126", "나무 계단 프리뷰"),
        "esc": ("PW-BLD-132", "나무 계단 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-133", "나무 계단 Tab 건축 중단 확인"),
    },
    {
        "item_name": "나무 벽",
        "tab_name": "건축",
        "tab_image": IMG_TAB_ARCHITECTURE,
        "representative_image": IMG_REP_ARCHITECTURE,
        "item_image": IMG_ITEM_WOOD_WALL,
        "preview": ("PW-BLD-134", "나무 벽 프리뷰"),
        "esc": ("PW-BLD-139", "나무 벽 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-140", "나무 벽 Tab 건축 중단 확인"),
    },
    {
        "item_name": "나무 문",
        "tab_name": "건축",
        "tab_image": IMG_TAB_ARCHITECTURE,
        "representative_image": IMG_REP_ARCHITECTURE,
        "item_image": IMG_ITEM_WOOD_DOOR,
        "preview": ("PW-BLD-141", "나무 문 프리뷰"),
        "esc": ("PW-BLD-146", "나무 문 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-147", "나무 문 Tab 건축 중단 확인"),
    },
    {
        "item_name": "사다리",
        "tab_name": "건축",
        "tab_image": IMG_TAB_ARCHITECTURE,
        "representative_image": IMG_REP_ARCHITECTURE,
        "item_image": IMG_ITEM_LADDER,
        "preview": ("PW-BLD-148", "사다리 프리뷰"),
        "esc": ("PW-BLD-153", "사다리 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-154", "사다리 Tab 건축 중단 확인"),
    },

    {
        "item_name": "경종",
        "tab_name": "방어",
        "tab_image": IMG_TAB_DEFENSE,
        "representative_image": IMG_REP_DEFENSE,
        "item_image": IMG_ITEM_ALARM_BELL,
        "preview": ("PW-BLD-162", "경종 프리뷰"),
        "esc": ("PW-BLD-167", "경종 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-168", "경종 Tab 건축 중단 확인"),
    },

    {
        "item_name": "나무 벽걸이 장식 선반",
        "tab_name": "가구",
        "tab_image": IMG_TAB_FURNITURE,
        "representative_image": IMG_REP_FURNITURE,
        "item_image": IMG_ITEM_WOOD_WALL_DECOR_SHELF,
        "preview": ("PW-BLD-169", "나무 벽걸이 장식 선반 프리뷰"),
        "esc": ("PW-BLD-174", "나무 벽걸이 장식 선반 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-175", "나무 벽걸이 장식 선반 Tab 건축 중단 확인"),
    },
    {
        "item_name": "앤티크 빨간색 카펫",
        "tab_name": "가구",
        "tab_image": IMG_TAB_FURNITURE,
        "representative_image": IMG_REP_FURNITURE,
        "item_image": IMG_ITEM_ANTIQUE_RED_CARPET,
        "preview": ("PW-BLD-176", "앤티크 빨간색 카펫 프리뷰"),
        "esc": ("PW-BLD-181", "앤티크 빨간색 카펫 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-182", "앤티크 빨간색 카펫 Tab 건축 중단 확인"),
    },
    {
        "item_name": "사각 탁자",
        "tab_name": "가구",
        "tab_image": IMG_TAB_FURNITURE,
        "representative_image": IMG_REP_FURNITURE,
        "item_image": IMG_ITEM_SQUARE_TABLE,
        "preview": ("PW-BLD-183", "사각 탁자 프리뷰"),
        "esc": ("PW-BLD-188", "사각 탁자 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-189", "사각 탁자 Tab 건축 중단 확인"),
    },
    {
        "item_name": "나무 의자",
        "tab_name": "가구",
        "tab_image": IMG_TAB_FURNITURE,
        "representative_image": IMG_REP_FURNITURE,
        "item_image": IMG_ITEM_WOOD_CHAIR,
        "preview": ("PW-BLD-190", "나무 의자 프리뷰"),
        "esc": ("PW-BLD-195", "나무 의자 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-196", "나무 의자 Tab 건축 중단 확인"),
    },
#     {
#         "item_name": "관엽식물",
#         "tab_name": "가구",
#         "tab_image": IMG_TAB_FURNITURE,
#         "representative_image": IMG_REP_FURNITURE,
#         "item_image": IMG_ITEM_HOUSEPLANT,
#         "scroll_down": True,
#         "preview": ("PW-BLD-197", "관엽식물 프리뷰"),
#         "esc": ("PW-BLD-202", "관엽식물 ESC 건축 중단 확인"),
#         "tab": ("PW-BLD-203", "관엽식물 Tab 건축 중단 확인"),
#     },

    {
        "item_name": "간판",
        "tab_name": "기타",
        "tab_image": IMG_TAB_MISC,
        "representative_image": IMG_REP_MISC,
        "item_image": IMG_ITEM_SIGNBOARD,
        "preview": ("PW-BLD-206", "간판 프리뷰"),
        "esc": ("PW-BLD-211", "간판 ESC 건축 중단 확인"),
        "tab": ("PW-BLD-212", "간판 Tab 건축 중단 확인"),
    },
]


# ---------------------------------------------------------
# PREVIEW_CASES 자동 생성
# ---------------------------------------------------------

PREVIEW_CASES = []

for target in BUILDING_PREVIEW_TARGETS:
    preview_id, preview_name = target["preview"]
    esc_id, esc_name = target["esc"]
    tab_id, tab_name = target["tab"]

    PREVIEW_CASES.append(
        (
            preview_id,
            preview_name,
            make_preview_case(
                target["tab_image"],
                target["representative_image"],
                target["tab_name"],
                target["item_image"],
                target["item_name"],
                target.get("scroll_down", False)
            )
        )
    )

    PREVIEW_CASES.append(
        (
            esc_id,
            esc_name,
            make_cancel_case(
                target["tab_image"],
                target["representative_image"],
                target["tab_name"],
                target["item_image"],
                target["item_name"],
                "ESC",
                target.get("scroll_down", False)
            )
        )
    )

    PREVIEW_CASES.append(
        (
            tab_id,
            tab_name,
            make_cancel_case(
                target["tab_image"],
                target["representative_image"],
                target["tab_name"],
                target["item_image"],
                target["item_name"],
                "TAB",
                target.get("scroll_down", False)
            )
        )
    )