# -*- coding: utf-8 -*-
"""
테스트 스텝 문구 기반의 1차 실행기입니다.

목표:
- 엑셀의 Candidate 케이스를 바로 1차 실행해볼 수 있게 만드는 것
- 이후 안정화되면 케이스별 전용 함수로 분리하는 것

주의:
- 이미지 alias가 없는 Test_Data는 실행 중 AssertionError가 날 수 있습니다.
- 이 경우 docs/image_capture_checklist.csv를 보고 이미지를 캡처하거나 config.py 좌표를 보강하세요.
"""

from airtest.core.api import keyevent, sleep

from common import build_mode


def split_test_data(value):
    if not value:
        return []
    text = str(value)
    parts = []
    for sep in ["/", ","]:
        if sep in text:
            for p in text.split(sep):
                p = p.strip()
                if p:
                    parts.append(p)
            return parts
    return [text.strip()]


def run_step(step):
    action = step.get("action") or ""
    data = step.get("test_data") or ""
    expected = step.get("expected_result") or ""
    labels = split_test_data(data)

    # 접속/월드 준비류: 수동 사전조건으로 간주
    if "월드에 접속" in action or "캐릭터 조작" in expected:
        return "SKIP_PRECONDITION"

    # 키 입력
    if "B 키" in data or "B 키" in action:
        build_mode.open_build_mode()
        return "OK"

    if "ESC 키" in data or "ESC 키" in action:
        build_mode.close_with_esc()
        return "OK"

    if "Tab 키" in data or "Tab" in action:
        build_mode.cancel_with_tab()
        return "OK"

    if "회전 입력" in data or "회전" in action:
        build_mode.press_rotate()
        return "OK"

    if "스냅" in data or "LCtrl" in data or "Ctrl" in data:
        build_mode.press_snap()
        return "OK"

    if "건축 입력" in data or "F 키" in data or "설치 확정" in data:
        build_mode.confirm_build()
        return "OK"

    if "시공 완료까지 대기" in data or "타이머" in action:
        build_mode.wait_until_timer_end()
        return "OK"

    # 좌표/fixture 이동
    for label in labels:
        if "위치" in label:
            build_mode.move_to_position(label)
            return "OK"

    # 탭 클릭
    if "탭을 클릭" in action or "탭 클릭" in action:
        for label in labels:
            if "탭 이미지" in label:
                build_mode.click_tab(label)
                return "OK"

    # 아이템/건축물 선택
    if "선택" in action or "클릭" in action:
        for label in labels:
            if "이미지" in label:
                build_mode.select_item(label)
                return "OK"

    # 이미지 검증
    if "확인" in action or "표시" in expected or "유지" in expected or "인식" in expected:
        for label in labels:
            if "이미지" in label:
                build_mode.assert_by_label(label)
                return "OK"

    sleep(0.5)
    return "NO_MATCH"
