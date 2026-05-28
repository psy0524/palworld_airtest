# -*- encoding=utf8 -*-
from airtest.core.api import *

import os
import sys

BASE_DIR = os.path.dirname(__file__)

if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

auto_setup(__file__, logdir=True)

connect_device("Windows:///")


from build_common import recover_to_default_state
from mode_cases import (
    tc_001_open_build_mode,
    tc_002_close_build_mode,
    tc_004_duplicate_open_build_mode,
)
from tab_cases import (
    tc_005_click_production_tab,
    tc_006_click_pal_tab,
    tc_007_click_storage_tab,
    tc_008_click_food_tab,
    tc_009_click_infra_tab,
    tc_010_click_lighting_tab,
    tc_011_click_architecture_tab,
    tc_012_click_defense_tab,
    tc_013_click_furniture_tab,
    tc_014_click_misc_tab,
)


def log_case_start(case_id, case_name):
    print("\n==============================")
    print(f"START: {case_id} / {case_name}")
    print("==============================")


def log_case_end(case_id, result="PASS"):
    print(f"END: {case_id} / {result}")
    snapshot(msg=f"{case_id}_{result}")


def run_case(case_id, case_name, func):
    """
    케이스 실행 공통 래퍼.
    실패 시에만 복구한다.
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


if __name__ == "__main__":

    TEST_CASES = [
        ("PW-BLD-001", "건축모드 창 열기", tc_001_open_build_mode),
        ("PW-BLD-002", "건축모드 창 닫기", tc_002_close_build_mode),
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
        sleep(1)