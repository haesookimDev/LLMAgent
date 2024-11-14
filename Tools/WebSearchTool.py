import base64
import time
import openai
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
from io import BytesIO
from selenium.webdriver.common.keys import Keys

class WebSearchTool:
    def __init__(self, openai_api_key):
        # OpenAI API 키 설정
        self.client = openai.OpenAI(api_key=openai_api_key)
        
        # Chrome 옵션 설정
        options = Options()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-extensions')
        options.add_argument('--headless')  # 브라우저 UI를 띄우지 않고 실행 (필요에 따라 설정)
        
        # ChromeDriver 설정 (webdriver_manager를 이용하여 자동으로 ChromeDriver 설치)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    def capture_screenshot_base64(self):
        # 스크린샷 캡처
        screenshot = self.driver.get_screenshot_as_png()
        # Base64로 인코딩
        screenshot_base64 = base64.b64encode(screenshot).decode('utf-8')
        return screenshot_base64
    
    def get_dom(self):
        # 현재 페이지의 DOM을 가져옴
        return self.driver.page_source
    
    def send_to_openai(self, screenshot_base64, dom, search):
        # OpenAI API에 데이터 전송
        response = self.client.chat.completions.create(
            model="gpt-4o",  # 또는 GPT-3 모델 사용 가능
            messages=[
        {"role": "system", "content": "당신은 웹 검색 에이전트 입니다. 주어진 프롬프트를 보고 순차적으로 답변하세요"},
        {"role": "user", "content": f"""Given the base64 screenshot and DOM below, 
            identify the position of the search box and suggest a suitable search query:{search}
            Screenshot:{screenshot_base64}
            , 
            """},
        ],
            max_tokens=150
        )
        return response['choices'][0]['text'].strip()
    
    def perform_search(self, search_query):
        # 검색창 찾기 (구글의 경우)
        search_box = self.driver.find_element(By.NAME, "q")
        
        # 검색어 입력
        search_box.send_keys(search_query)
        
        # 엔터 키로 검색 실행
        search_box.send_keys(Keys.RETURN)
        
        # 검색 결과 페이지 로딩 대기
        time.sleep(3)
        
        # 검색 결과 추출 (최대 3개의 링크 추출)
        results = self.driver.find_elements(By.CSS_SELECTOR, 'h3')
        links = []
        for result in results[:3]:
            link = result.find_element(By.XPATH, '..').get_attribute('href')
            links.append(link)
        
        return links
    
    def search_and_execute(self, url):
        # 웹 페이지 열기
        self.driver.get(url)
        
        # 스크린샷을 Base64로 인코딩
        screenshot_base64 = self.capture_screenshot_base64()
        
        # DOM 정보 추출
        dom = self.get_dom()
        
        # OpenAI API에 요청하여 검색창 위치와 검색어 받아오기
        suggested_search_query = self.send_to_openai(screenshot_base64, dom, "서울시 인구수")
        
        # 반환된 검색어로 검색 실행
        search_results = self.perform_search(suggested_search_query)
        
        print(f"Suggested search query: {suggested_search_query}")
        print("Top 3 search results:")
        for link in search_results:
            print(link)
    
    def close_browser(self):
        # 브라우저 종료
        self.driver.quit()


# 사용 예시
if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    import asyncio

    load_dotenv('Config/.env')

    openai_api_key = os.getenv('OPENAI_API_KEY')  # OpenAI API 키 입력
    tool = WebSearchTool(openai_api_key)
    
    # 구글 검색 페이지 예시
    tool.search_and_execute("https://www.google.com")
    
    # 브라우저 종료
    tool.close_browser()
