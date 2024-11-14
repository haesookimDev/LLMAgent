# 웹 에이전트 구현하기

### 1. Function calling을 통한 단순 검색 선행
### 2. 구현할 시스템 구조도 그리기
    - 구글 검색에서 화면 캡처 및 현재 HTML 추출 후 LLM에 전송
    - LLM이 검색어와 검색어를 입력할 수 있는 HTML 태그 전송
    - 전송된 것을 기반으로 Tool call 
    - Tool에 전송받은 파라미터를 입력해 실행 
    - 검색 결과를 다시 LLM에 전송
    - 웹사이트 클릭 혹은 재검색
    - 위 과정을 threshold 정도 반복
    - 이후 종료 혹은 사용자의 보완 피드백 후 다시 수행
### 3. 웹 에이전트를 위한 Tools(Function) 설계
### 4. 각 Tools의 결과에 따른 Agent의 Actions 설계
### 5. 그 왜 데이터 전처리 등을 위한 Utills 구현
### 6. 테스트

# 해야 할 일 순서대로 정리

## 1. **Tools 구현**
- [ ] **Web Search Tool** 구현
  - 구글 검색을 통해 결과를 가져오는 기능.
- [ ] **HTML Extraction Tool** 구현
  - HTML 태그에서 필요한 데이터를 추출하는 기능.
- [ ] **Screenshot Tool** 구현
  - 웹 페이지의 스크린샷을 캡처하는 기능.
- [ ] **Interaction Tool** 구현
  - 웹 페이지 내 동작(클릭, 입력 등)을 수행하는 기능.
- [ ] **Data Preprocessing Tool** 구현
  - 데이터를 LLM에 전달하기 전에 정리하고 형식을 맞추는 기능.
- [ ] **Tool Execution Manager** 구현
  - LLM의 요청에 따라 적절한 Tool을 호출하고 결과를 반환하는 기능.
- [ ] **Feedback Integration Tool** 구현
  - 사용자 피드백을 처리하고 검색 결과를 수정하거나 재시도하는 기능.
- [ ] **Error Logging Tool** 구현
  - 각 Tool 호출 중 발생한 에러를 기록하는 기능.

---

## 2. **Actions 구현**
- [ ] **Perform Search** 구현
  - 사용자가 입력한 검색어로 웹 검색을 수행하고 결과를 수집하는 기능.
- [ ] **Extract and Analyze HTML** 구현
  - HTML 태그에서 데이터를 추출하고 분석하여 필요한 정보 요약.
- [ ] **Take Screenshot** 구현
  - 웹 페이지의 스크린샷을 찍고 LLM에 전달하는 기능.
- [ ] **Interact with Website** 구현
  - LLM으로부터 받은 요청에 따라 웹사이트 내에서 동작을 수행하는 기능.
- [ ] **Refine Search or Navigate** 구현
  - 검색 결과를 바탕으로 재검색하거나 링크를 클릭하여 탐색하는 기능.
- [ ] **Loop and Iterate** 구현
  - 검색 및 탐색을 반복하여 최적의 결과를 얻는 기능.
- [ ] **Handle Feedback** 구현
  - 사용자 피드백을 바탕으로 작업을 수정하거나 재시도하는 기능.
- [ ] **Log Results** 구현
  - 모든 결과를 로그로 기록하고 저장하는 기능.

---

## 3. **Utils 구현**
- [ ] **Data Cleaning Utility** 구현
  - 데이터를 정리하고 불필요한 정보를 제거하는 기능.
- [ ] **JSON Formatter Utility** 구현
  - 데이터를 JSON 형식으로 변환하는 기능.
- [ ] **String Normalizer** 구현
  - 텍스트를 정규화하여 표준화된 형식으로 변환하는 기능.
- [ ] **URL Validator** 구현
  - URL의 유효성을 검사하고 잘못된 URL을 수정하는 기능.
- [ ] **Log Formatter** 구현
  - 로그 메시지를 일정한 형식으로 포맷팅하는 기능.
- [ ] **Parameter Validator** 구현
  - LLM에서 받은 파라미터의 유효성을 검사하는 기능.
- [ ] **HTML Compressor** 구현
  - HTML 소스를 압축하여 작은 크기로 만드는 기능.
- [ ] **Timer Utility** 구현
  - 작업 실행 시간을 측정하는 기능.
- [ ] **Retry Mechanism Utility** 구현
  - 작업 실패 시 재시도하는 기능.
- [ ] **File I/O Utility** 구현
  - 파일 입출력을 처리하는 기능.

---

## 4. **전체 통합 및 테스트**
- [ ] **Tools 단위 테스트** 진행
  - 각 Tool이 독립적으로 정상 동작하는지 테스트.
- [ ] **Actions 통합 테스트** 진행
  - Actions가 Tools를 올바르게 호출하고 동작하는지 테스트.
- [ ] **전체 시스템 테스트** 진행
  - 전체 에이전트 워크플로우가 예상대로 작동하는지 확인.
- [ ] **성능 최적화** 진행
  - 시스템의 성능을 분석하고 필요한 최적화 작업 수행.
- [ ] **에러 처리 및 로깅** 검토
  - 에러 처리 및 로깅 기능이 적절히 동작하는지 확인.
