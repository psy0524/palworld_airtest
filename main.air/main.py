# -*- coding: utf-8 -*-
from airtest.core.api import *
import json
from pathlib import Path
import traceback

from common.build_mode import set_image_aliases, recover_to_default_state
from common.executor import run_step

auto_setup(__file__)

BASE_DIR = Path(__file__).resolve().parent
CASES_PATH = BASE_DIR / "cases" / "candidate_cases.json"
ALIASES_PATH = BASE_DIR / "image_aliases.json"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def run_case(case):
    print(f"\n[CASE START] {case['case_id']} | {case['case_name']}")
    for step in case.get("steps", []):
        step_no = step.get("step_no")
        action = step.get("action")
        print(f"  - Step {step_no}: {action}")
        result = run_step(step)
        print(f"    result={result}")
    print(f"[CASE END] {case['case_id']}")


def main():
    set_image_aliases(load_json(ALIASES_PATH))
    cases = load_json(CASES_PATH)

    failed = []
    for case in cases:
        try:
            run_case(case)
        except Exception as e:
            failed.append({"case_id": case["case_id"], "case_name": case["case_name"], "error": str(e)})
            print(f"[CASE FAIL] {case['case_id']} | {e}")
            traceback.print_exc()
        finally:
            recover_to_default_state()

    print("\n===== RUN SUMMARY =====")
    print(f"total={len(cases)}, failed={len(failed)}")
    for item in failed:
        print(f"- {item['case_id']} {item['case_name']}: {item['error']}")


if __name__ == "__main__":
    main()
