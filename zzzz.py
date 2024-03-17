# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

def decode_unicode_escape(s):
    return bytes(s, 'utf-8').decode('unicode-escape')

# 크롬 드라이버의 경로 (다운로드 받은 드라이버 경로로 수정)
chrome_driver_path = 'C:\\chromedriver_win32\\chromedriver.exe'

# 크롬 브라우저 옵션 설정
chrome_options = webdriver.ChromeOptions()
#크롬 드라이버 버전 버전 114.0.5735.110(공식 빌드) (64비트)
# 크롬 드라이버 생성
driver = webdriver.Chrome()
# 웹 페이지 열기
driver.get("https://gyeonggi.childcare.go.kr/ccef/nursery/NurserySlPL.jsp")  # 실제 웹페이지 주소로 수정

# Select 객체 생성
select_element = Select(driver.find_element(By.ID, "signgu"))  # 수정된 부분

# 옵션 선택 (예시로 첫 번째 옵션 선택)
select_element.select_by_index(19)


# Select 객체 생성
select_element = Select(driver.find_element(By.ID, "crtype"))  # 수정된 부분

# 옵션 선택 (예시로 첫 번째 옵션 선택)
select_element.select_by_index(4)

# 클릭
button_element = driver.find_element(By.CLASS_NAME, "button")
button_element.click()
i=1
count= 0
wait = WebDriverWait(driver, 10)
# 크롤링
def crolling():
    for i in range(1, 11):  # 예시로 1부터 9까지의 행을 반복
        xpath = f'tbody > tr:nth-child({i}) > td.lef > a'
        kindergarten_name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, xpath)))
    
    
    
        #print(f"Clicking on:  "+str(i))
        count = i+1
        kindergarten_name_element.click()

        # 어린이집 상세 정보 페이지로 이동

        # 현재 창의 핸들을 저장
        main_window_handle = driver.window_handles[0]

        # 새로 열린 창의 핸들을 얻음
        new_window_handle = driver.window_handles[1]

        # 새로 열린 창으로 이동
        driver.switch_to.window(new_window_handle)

        # 여기서 새 창에서 필요한 작업을 수행
        translated_name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#popWrap2 > div > div > div > table > tbody > tr:nth-child(1) > td.td_left')))
        translated_name_text = translated_name_element.text
        

        translated_name_element_2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#popWrap2 > div > div > div > table > tbody > tr:nth-child(10) > td.td_left')))
        translated_name_text_2 = translated_name_element_2.text
        print(f"어린이집 : {translated_name_text}    " + f"주소: { translated_name_text_2 }" )
       

   
    
   
        #    예: 주소 크롤링, 다운로드 등

        # 새 창에서 필요한 작업이 끝난 후, 새 창 닫기
        time.sleep(1)
        driver.close()

        # 다시 메인 창으로 이동
        driver.switch_to.window(main_window_handle)

while True:
    try:
        crolling()
        next_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "next")))
        next_button.click()
    except Exception as e:
        print("No more pages available.")
        break  # Exit the loop if there are no more pages
        
# 브라우저 종료




