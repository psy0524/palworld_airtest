# Palworld Build Mode AirTest Automation

## 프로젝트 소개

본 프로젝트는 Palworld 건축 모드(Build Mode)의 주요 기능을 AirTest를 활용하여 자동화 테스트하기 위한 프로젝트입니다.

건축 모드 진입부터 탭 이동, 건축물 선택, 프리뷰 진입, 건축 취소(ESC/TAB) 동작까지 자동으로 검증할 수 있도록 설계하였습니다.

---

## 테스트 범위

### 건축 모드

* 건축 모드 진입
* 건축 모드 종료
* 건축 모드 중복 진입

### 탭 이동

* 생산 탭
* 팰 탭
* 수납 탭
* 식료품 탭
* 인프라 탭
* 조명 탭
* 건축 탭
* 방어 탭
* 가구 탭
* 기타 탭

### 건축물 프리뷰

각 탭의 대표 건축물을 대상으로 다음 항목을 검증합니다.

* 건축물 선택
* 프리뷰 UI 표시 여부 확인
* ESC 입력 시 건축 취소
* TAB 입력 시 건축 취소

---

## 프로젝트 구조

```text
main.py
 ├─ build_common.py
 ├─ input_utils.py
 ├─ config.py
 ├─ images.py
 ├─ mode_cases.py
 ├─ tab_cases.py
 ├─ preview_cases.py
 └─ suites.py
```

### build_common.py

공통 기능 관리

* 건축 모드 진입
* 건축 모드 종료
* 복구 로직
* 탭 이동

### input_utils.py

게임 입력 제어

* 키 입력
* ESC
* TAB
* B
* F

### images.py

AirTest Template 이미지 관리

* 탭 이미지
* 대표 건축물 이미지
* 건축물 이미지
* 프리뷰 UI 이미지

### mode_cases.py

건축 모드 관련 테스트 케이스

### tab_cases.py

탭 이동 관련 테스트 케이스

### preview_cases.py

건축물 프리뷰 관련 테스트 케이스

### suites.py

실행 대상 테스트 스위트 관리

---

## 자동화 방식

### 이미지 인식 기반

AirTest Template Matching을 사용하여 UI 요소를 식별합니다.

검증 대상

* 건축 모드 창
* 탭
* 대표 건축물
* 건축물 아이콘
* 프리뷰 UI

### 상태 복구

테스트 실패 시 자동 복구를 수행합니다.

예시

* 건축 모드가 열린 상태로 종료된 경우
* ESC 입력 후 기본 상태 복귀

---

## 실행 방법

### Smoke Test

```python
RUN_TARGET = "smoke"
```

### Build Mode Test

```python
RUN_TARGET = "mode"
```

### Tab Test

```python
RUN_TARGET = "tab"
```

### Preview Test

```python
RUN_TARGET = "preview"
```

### Full Test

```python
RUN_TARGET = "all"
```

---

## 구현 완료 항목

### Automated

* 건축 모드 진입
* 건축 모드 종료
* 건축 모드 중복 진입
* 전체 탭 이동
* 건축물 프리뷰 진입
* ESC 건축 취소
* TAB 건축 취소

### Candidate

* 스크롤이 필요한 건축물 자동화
* 화면 위치 의존성이 높은 건축물
* 추가 프리뷰 검증

### Manual

* 실제 건축 배치 검증
* 충돌 판정 검증
* 자원 부족 검증
* 설치 가능/불가능 조건 검증
* 위치 제약 검증

---

## 사용 기술

* Python
* AirTest
* OpenCV
* Template Matching
* Windows Automation

---

## 목적

반복 수행되는 건축 모드 테스트를 자동화하여 테스트 시간을 단축하고, 회귀 테스트 수행 시 일관된 결과를 확보하는 것을 목표로 합니다.
