# -*- coding: utf-8 -*-
"""
Palworld Build Mode AirTest 설정 파일

좌표는 PC 해상도, 게임 창 위치, UI 배율에 따라 달라질 수 있습니다.
처음 실행 전 본인 환경 기준으로 수정하세요.
"""

TIMEOUT_SHORT = 3
TIMEOUT_DEFAULT = 8
TIMEOUT_LONG = 30

# 키 입력
KEY_BUILD_MODE = "b"
KEY_ESC = "esc"
KEY_TAB = "tab"
KEY_ROTATE = "r"
KEY_CONFIRM_BUILD = "f"
KEY_SNAP = "ctrl"

# 좌표 fixture: 실제 게임 환경에서 AirTest IDE로 좌표 확인 후 수정
POSITIONS = {
    "설치 가능 기준 위치": (960, 540),
    "벽 없는 테스트 위치": (960, 540),
    "벽 설치 fixture 위치": (960, 540),
    "바닥 없는 테스트 위치": (960, 540),
    "바닥 설치 fixture 위치": (960, 540),
    "토대 없는 테스트 위치": (960, 540),
    "토대 설치 fixture 위치": (960, 540),
    "충돌 검증 fixture 위치": (960, 540),
}

# 이미지 인식 정확도
THRESHOLD_DEFAULT = 0.80
