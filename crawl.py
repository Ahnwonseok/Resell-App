from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def resell():
    columns=['브랜드', '상품명', '즉시구매가', '거래량','저장수'] 

    #창 숨기는 옵션 
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome("chromedriver",options=options)
    count = 0

    driver.get("https://kream.co.kr/exhibitions/249")

    time.sleep(2)

    brand=driver.find_elements(By.CLASS_NAME,f'product_info_brand.brand')#브랜드
    review=driver.find_elements(By.CLASS_NAME,f'review_figure')#리뷰수    
    name=driver.find_elements(By.CLASS_NAME,f'translated_name')#상품명
    price=driver.find_elements(By.CLASS_NAME,f'amount')#즉시구매가
    save=driver.find_elements(By.CLASS_NAME,f'wish_figure')#저장수
    
    print(review[0].text)
    print(brand[0].text)
    print(name[0].text)
    print(price[0].text)
    print(save[0].text)
    
    dicts={i : 0 for i in range(5)}
    value = []
    for i in range(10):    
        value.append(brand[i].text)
        value.append(name[i].text)
        value.append(price[i].text)
        value.append(review[i].text)
        value.append(save[i].text)
        
    return value