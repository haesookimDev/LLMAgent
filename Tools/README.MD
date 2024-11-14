1. Web Search Tool  
    기능:  
        Google에서 검색어를 입력하고 결과를 가져오는 기능.  
    입력:  
        검색어 (query), 옵션 (언어, 결과 개수 등).  
    출력:  
        검색 결과의 HTML 소스.  
        페이지 요약 또는 링크 리스트.  
    사용 라이브러리:  
        selenium (브라우저 자동화)  
        requests + BeautifulSoup (HTML 파싱)  
  
2. HTML Extraction Tool  
    기능:  
        특정 HTML 태그 또는 구조에서 데이터를 추출.  
    입력:  
        HTML 소스 (html_content).  
        태그 정보 (tag, attributes).  
    출력:  
        추출된 텍스트, URL, 또는 태그 속성 값.  
    사용 라이브러리:  
        BeautifulSoup (HTML 파싱)  

3. Screenshot Tool  
    기능:  
        현재 페이지의 스크린샷을 저장.  
    입력:  
        브라우저 인스턴스 또는 URL.  
    출력:  
        이미지 파일 (PNG/JPEG).  
    사용 라이브러리:  
        selenium (브라우저 캡처)  
  
4. Interaction Tool  
    기능:  
        웹사이트 내에서 클릭, 입력, 스크롤 동작 수행.  
    입력:  
        HTML 태그 및 속성 정보.  
        수행할 동작 (click, input, scroll).  
    출력:  
        동작 결과 페이지의 HTML 소스.  
    사용 라이브러리:  
        selenium  
  
5. Data Preprocessing Tool  
    기능:  
        HTML 또는 텍스트 데이터를 LLM이 처리할 수 있는 형식으로 변환.  
    입력:  
        원시 HTML, 텍스트.  
    출력:  
        구조화된 JSON 또는 텍스트 데이터.  
    사용 라이브러리:  
        Python 기본 처리 함수 (json, re).  
  
6. Tool Execution Manager  
    기능:  
        LLM의 요청에 따라 적절한 Tool 호출 및 결과 반환.  
    입력:  
        LLM에서 전달된 요청 정보 (Tool 이름, 파라미터).  
    출력:  
        Tool 실행 결과.  
    설계 고려사항:  
        각 Tool의 입력 및 출력을 유효성 검사.  
        에러 처리 (예: 잘못된 태그 요청 시 기본 응답 반환).  
  
7. Feedback Integration Tool  
    기능:  
        사용자 피드백을 받아 작업 재시도 또는 수정 수행.  
    입력:  
        사용자 입력 (수정 사항, 재검색 요청 등).  
        현재 상태 (검색 결과, HTML 소스).  
    출력:  
        갱신된 검색 결과 또는 HTML 소스.  
  
8. Error Logging Tool  
    기능:  
        모든 Tool 사용 과정에서 발생한 에러를 로깅.  
    입력:  
        에러 메시지, Tool 이름, 입력 데이터.  
    출력:  
        로그 파일 또는 시스템 출력.  