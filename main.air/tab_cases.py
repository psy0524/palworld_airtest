# -*- encoding=utf8 -*-

from build_common import open_build_mode, click_tab
from images import (
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