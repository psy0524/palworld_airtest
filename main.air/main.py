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
from suites import SUITES


# 실행할 묶음 선택
# "mode", "tab", "smoke", "preview", "all" 중 선택
RUN_TARGET = "all"


def log_case_start(case_id, case_name):
    print("\n==============================")
    print(f"START: {case_id} / {case_name}")
    print("==============================")


def log_case_end(case_id, result="PASS"):
    print(f"END: {case_id} / {result}")
    snapshot(msg=f"{case_id}_{result}")


def run_case(case_id, case_name, func):
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

    TEST_CASES = SUITES[RUN_TARGET]

    print(f"실행 대상: {RUN_TARGET}")
    print(f"실행 케이스 수: {len(TEST_CASES)}")

    for case_id, case_name, case_func in TEST_CASES:
        run_case(case_id, case_name, case_func)
        sleep(1)