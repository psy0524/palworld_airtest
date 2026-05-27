# Palworld 건축모드 AirTest 자동화 Starter

이 패키지는 첨부된 테스트케이스 파일에서 `Candidate`로 분류된 케이스를 기준으로 만든 **자동화 시작용 프로젝트 구조**입니다.

## 현재 구성

- 전체 케이스: 229개
- 자동화 후보 Candidate: 100개
- Manual: 129개
- Automated: 0개

## 추천 진행 순서

1. `docs/image_capture_checklist.csv`를 보고 필요한 기준 이미지를 캡처합니다.
2. 캡처한 이미지를 `main.air/images/` 하위 폴더에 넣습니다.
3. `main.air/config.py`에서 좌표와 타임아웃을 본인 환경에 맞게 수정합니다.
4. `main.air/main.py`를 실행해 Candidate 케이스를 순차 실행합니다.
5. 안정적으로 통과한 케이스만 엑셀의 자동화 상태를 `Automated`로 변경합니다.

## 실행 예시

```bash
pip install -r requirements.txt
airtest run main.air --log logs
airtest report main.air --log_root logs --outfile report.html
```

## 중요한 기준

현재는 완성된 AirTest 코드가 없으므로 엑셀 상태는 `Candidate`가 맞습니다.  
아래 조건을 만족한 케이스만 `Automated`로 올리는 것을 권장합니다.

1. 코드 작성 완료
2. 단독 실행 성공
3. 전체 실행 중에도 성공
4. 3회 이상 반복 실행 시 결과 안정
5. 실패 시 로그/스크린샷으로 원인 확인 가능
