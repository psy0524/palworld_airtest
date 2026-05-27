# -*- encoding=utf8 -*-
from airtest.core.api import *

auto_setup(__file__)

# =========================================================
# Palworld 건축 모드 AirTest 자동화 - 1차 Starter
# 대상: PW-BLD-001 ~ PW-BLD-014
# 범위: 건축 모드 열기/닫기, 탭 클릭 확인
# =========================================================


# ---------------------------------------------------------
# 1. AirTest IDE 스크린샷 캡처 후 여기에 Template 등록
# ---------------------------------------------------------
# 아래 Template들은 AirTest IDE에서 직접 캡처한 이미지로 교체하면 됨.
# 예: AirTest IDE에서 assert_exists 버튼 클릭 → 화면 영역 드래그
# 그러면 Template(r"tpl1778xxxx.png") 코드가 자동 생성됨.

IMG_BUILD_MODE_WINDOW = Template(r"tpl_build_mode_window.png")
IMG_DEFAULT_HUD = Template(r"tpl_default_hud.png")

IMG_TAB_PRODUCTION = Template(r"tpl_tab_production.png")
IMG_TAB_PAL = Template(r"tpl_tab_pal.png")
IMG_TAB_STORAGE = Template(r"tpl_tab_storage.png")
IMG_TAB_FOOD = Template(r"tpl_tab_food.png")
IMG_TAB_INFRA = Template(r"tpl_tab_infra.png")
IMG_TAB_LIGHTING = Template(r"tpl_tab_lighting.png")
IMG_TAB_ARCHITECTURE = Template(r"tpl_tab_architecture.png")
IMG_TAB_DEFENSE = Template(r"tpl_tab_defense.png")
IMG_TAB_FURNITURE = Template(r"tpl_tab_furniture.png")
IMG_TAB_MISC = Template(r"tpl_tab_misc.png")

# 탭 클릭 후 실제로 해당 탭이 열렸는지 확인할 대표 이미지
IMG_REP_PRODUCTION = Template(r"tpl_rep_production.png")
IMG_REP_PAL = Template(r"tpl_rep_pal.png")
IMG_REP_STORAGE = Template(r"tpl_rep_storage.png")
IMG_REP_FOOD = Template(r"tpl_rep_food.png")
IMG_REP_INFRA = Template(r"tpl_rep_infra.png")
IMG_REP_LIGHTING = Template(r"tpl_rep_lighting.png")
IMG_REP_ARCHITECTURE = Template(r"tpl_rep_architecture.png")
IMG_REP_DEFENSE = Template(r"tpl_rep_defense.png")
IMG_REP_FURNITURE = Template(r"tpl_rep_furniture.png")
IMG_REP_MISC = Template(r"tpl_rep_misc.png")


# ---------------------------------------------------------
# 2. 공통 함수
# ---------------------------------------------------------

def log_case_start(case_id, case_name):
    print("\n==============================")
    print(f"START: {case_id} / {case_name}")
    print("==============================")


def log_case_end(case_id, result="PASS"):
    print(f"END: {case_id} / {result}")
    snapshot(msg=f"{case_id}_{result}")


def open_build_mode():
    """
    B 키 입력 후 건축 모드 창이 표시되는지 확인
    """
    keyevent("b")
    sleep(1)

    assert_exists(
        IMG_BUILD_MODE_WINDOW,
        "건축 모드 창이 표시되어야 한다."
    )


def close_build_mode():
    """
    ESC 키 입력 후 일반 HUD 또는 건축 모드가 닫힌 상태 확인
    """
    keyevent("esc")
    sleep(1)

    assert_exists(
        IMG_DEFAULT_HUD,
        "건축 모드가 닫히고 일반 HUD 상태여야 한다."
    )


def recover_to_default_state():
    """
    다음 케이스 실행을 위한 기본 복구 함수
    실패해도 다음 테스트가 진행될 수 있게 최대한 기본 상태로 돌림
    """
    try:
        keyevent("esc")
        sleep(0.5)
        keyevent("esc")
        sleep(0.5)
    except Exception as e:
        print(f"복구 중 예외 발생: {e}")


def click_tab(tab_image, representative_image, tab_name):
    """
    탭 클릭 후 해당 탭의 대표 건축물/아이콘이 보이는지 확인
    """
    touch(tab_image)
    sleep(0.8)

    assert_exists(
        representative_image,
        f"{tab_name} 탭 대표 항목이 표시되어야 한다."
    )


def run_case(case_id, case_name, func):
    """
    케이스 실행 공통 래퍼
    실패 시 스크린샷 남기고 기본 복구 시도
    """
    log_case_start(case_id, case_name)

    try:
        func()
        log_case_end(case_id, "PASS")

    except Exception as e:
        print(f"FAIL: {case_id} / {case_name}")
        print(e)
        snapshot(msg=f"{case_id}_FAIL")
        recover_to_default_state()
        raise


# ---------------------------------------------------------
# 3. 테스트 케이스 함수
# ---------------------------------------------------------

def tc_001_open_build_mode():
    open_build_mode()


def tc_002_close_build_mode():
    open_build_mode()
    close_build_mode()


def tc_003_preview_cancel_reopen():
    """
    1차에서는 프리뷰까지 가지 않고,
    건축 모드 닫기 후 재진입 안정성만 먼저 확인
    """
    open_build_mode()
    keyevent("esc")
    sleep(1)
    open_build_mode()


def tc_004_duplicate_open_build_mode():
    """
    건축 모드가 열린 상태에서 B 키를 한 번 더 눌렀을 때
    UI가 비정상적으로 깨지지 않는지 확인
    """
    open_build_mode()
    keyevent("b")
    sleep(1)

    assert_exists(
        IMG_BUILD_MODE_WINDOW,
        "건축 모드 중복 진입 후에도 건축 모드 창이 유지되어야 한다."
    )


def tc_005_click_production_tab():
    open_build_mode()
    click_tab(IMG_TAB_PRODUCTION, IMG_REP_PRODUCTION, "생산")


def tc_006_click_pal_tab():
    open_build_mode()
    click_tab(IMG_TAB_PAL, IMG_REP_PAL, "팰")


def tc_007_click_storage_tab():
    open_build_mode()
    click_tab(IMG_TAB_STORAGE, IMG_REP_STORAGE, "수납")


def tc_008_click_food_tab():
    open_build_mode()
    click_tab(IMG_TAB_FOOD, IMG_REP_FOOD, "식료품")


def tc_009_click_infra_tab():
    open_build_mode()
    click_tab(IMG_TAB_INFRA, IMG_REP_INFRA, "인프라")


def tc_010_click_lighting_tab():
    open_build_mode()
    click_tab(IMG_TAB_LIGHTING, IMG_REP_LIGHTING, "조명")


def tc_011_click_architecture_tab():
    open_build_mode()
    click_tab(IMG_TAB_ARCHITECTURE, IMG_REP_ARCHITECTURE, "건축")


def tc_012_click_defense_tab():
    open_build_mode()
    click_tab(IMG_TAB_DEFENSE, IMG_REP_DEFENSE, "방어")


def tc_013_click_furniture_tab():
    open_build_mode()
    click_tab(IMG_TAB_FURNITURE, IMG_REP_FURNITURE, "가구")


def tc_014_click_misc_tab():
    open_build_mode()
    click_tab(IMG_TAB_MISC, IMG_REP_MISC, "기타")


# ---------------------------------------------------------
# 4. 실행부
# ---------------------------------------------------------

if __name__ == "__main__":

    TEST_CASES = [
        ("PW-BLD-001", "건축모드 창 열기", tc_001_open_build_mode),
        ("PW-BLD-002", "건축모드 창 닫기", tc_002_close_build_mode),
        ("PW-BLD-003", "프리뷰취소후재진입", tc_003_preview_cancel_reopen),
        ("PW-BLD-004", "건축모드중복진입", tc_004_duplicate_open_build_mode),
        ("PW-BLD-005", "생산탭클릭", tc_005_click_production_tab),
        ("PW-BLD-006", "팰탭클릭", tc_006_click_pal_tab),
        ("PW-BLD-007", "수납탭클릭", tc_007_click_storage_tab),
        ("PW-BLD-008", "식료품탭클릭", tc_008_click_food_tab),
        ("PW-BLD-009", "인프라탭클릭", tc_009_click_infra_tab),
        ("PW-BLD-010", "조명탭클릭", tc_010_click_lighting_tab),
        ("PW-BLD-011", "건축탭클릭", tc_011_click_architecture_tab),
        ("PW-BLD-012", "방어탭클릭", tc_012_click_defense_tab),
        ("PW-BLD-013", "가구탭클릭", tc_013_click_furniture_tab),
        ("PW-BLD-014", "기타탭클릭", tc_014_click_misc_tab),
    ]

    for case_id, case_name, case_func in TEST_CASES:
        run_case(case_id, case_name, case_func)
        recover_to_default_state()
        sleep(1)