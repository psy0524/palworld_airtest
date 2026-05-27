# -*- coding: utf-8 -*-
from airtest.core.api import keyevent, touch, sleep

from config import (
    KEY_BUILD_MODE,
    KEY_ESC,
    KEY_TAB,
    KEY_ROTATE,
    KEY_CONFIRM_BUILD,
    KEY_SNAP,
    POSITIONS,
    TIMEOUT_LONG,
)
from common.image_utils import assert_image, touch_image, wait_image, image_exists


# 이 alias는 main.py에서 image_aliases.json으로 주입됩니다.
IMAGE_ALIASES = {}


def set_image_aliases(mapping: dict):
    global IMAGE_ALIASES
    IMAGE_ALIASES = mapping or {}


def resolve_image(label: str):
    return IMAGE_ALIASES.get(label)


def open_build_mode():
    keyevent(KEY_BUILD_MODE)
    path = resolve_image("건축 모드 창 이미지")
    if path:
        assert_image(path, "건축 모드 창이 표시되어야 함")


def close_with_esc():
    keyevent(KEY_ESC)


def cancel_with_tab():
    keyevent(KEY_TAB)


def press_rotate():
    keyevent(KEY_ROTATE)


def press_snap():
    keyevent(KEY_SNAP)


def confirm_build():
    keyevent(KEY_CONFIRM_BUILD)


def click_tab(label: str):
    path = resolve_image(label)
    if not path:
        raise AssertionError(f"탭 이미지 alias가 없습니다: {label}")
    touch_image(path)


def select_item(label: str):
    path = resolve_image(label)
    if not path:
        raise AssertionError(f"아이템 이미지 alias가 없습니다: {label}")
    touch_image(path)


def assert_by_label(label: str, message: str = ""):
    path = resolve_image(label)
    if not path:
        raise AssertionError(f"검증 이미지 alias가 없습니다: {label}")
    assert_image(path, message or label)


def move_to_position(label: str):
    if label not in POSITIONS:
        raise AssertionError(f"fixture 좌표가 config.py에 없습니다: {label}")
    touch(POSITIONS[label])


def wait_until_timer_end():
    # 실제 시공 완료 기준 이미지가 준비되면 이 로직을 더 엄격하게 바꾸세요.
    completed = resolve_image("설치 완료 건축물 이미지")
    if completed:
        wait_image(completed, timeout=TIMEOUT_LONG, message="설치 완료 건축물 대기")
    else:
        sleep(3)


def recover_to_default_state():
    """실패 후 다음 케이스에 영향을 줄이지 않도록 기본 상태로 복구합니다."""
    keyevent(KEY_ESC)
    sleep(0.5)
    keyevent(KEY_ESC)
    sleep(0.5)
