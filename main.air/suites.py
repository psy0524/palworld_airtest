# -*- encoding=utf8 -*-

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

from preview_cases import PREVIEW_CASES

MODE_CASES = [
    ("PW-BLD-001", "건축모드 창 열기", tc_001_open_build_mode),
    ("PW-BLD-002", "건축모드 창 닫기", tc_002_close_build_mode),
    ("PW-BLD-004", "건축모드중복진입", tc_004_duplicate_open_build_mode),
]


TAB_CASES = [
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

SMOKE_CASES = [
    ("PW-BLD-001", "건축모드 창 열기", tc_001_open_build_mode),
    ("PW-BLD-005", "생산탭클릭", tc_005_click_production_tab),
    ("PW-BLD-006", "팰탭클릭", tc_006_click_pal_tab),
]


ALL_CASES = (
    MODE_CASES
    + TAB_CASES
    + PREVIEW_CASES
)


SUITES = {
    "mode": MODE_CASES,
    "tab": TAB_CASES,
    "smoke": SMOKE_CASES,
    "preview": PREVIEW_CASES,
    "all": ALL_CASES,
}