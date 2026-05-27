# -*- coding: utf-8 -*-
from airtest.core.api import Template, exists, wait, assert_exists, touch
from pathlib import Path

from config import THRESHOLD_DEFAULT, TIMEOUT_DEFAULT

BASE_DIR = Path(__file__).resolve().parents[1]
IMAGE_DIR = BASE_DIR / "images"


def img(path: str, threshold: float = THRESHOLD_DEFAULT):
    """images/ 기준 상대 경로를 AirTest Template 객체로 변환합니다."""
    return Template(str(IMAGE_DIR / path), threshold=threshold)


def wait_image(path: str, timeout: int = TIMEOUT_DEFAULT, message: str = ""):
    message = message or f"이미지 확인: {path}"
    return wait(img(path), timeout=timeout)


def assert_image(path: str, message: str = ""):
    message = message or f"이미지가 화면에 표시되어야 함: {path}"
    return assert_exists(img(path), message)


def touch_image(path: str, timeout: int = TIMEOUT_DEFAULT):
    pos = wait_image(path, timeout=timeout, message=f"터치 대상 이미지 대기: {path}")
    touch(pos)
    return pos


def image_exists(path: str):
    return exists(img(path))
