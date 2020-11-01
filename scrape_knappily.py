from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options 
import time
from bs4 import BeautifulSoup
import csv

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

res_cate = []
category = ['Technology','Society','On%20this%20day','Environment','Politics','Law','Burning%20Issues','Business','World','Ethics','Sports','Literature','Lifestyle','Personalities']

for item in category:
    url = "https://knappily.com/"+item
    driver = webdriver.Chrome(options=chrome_options, executable_path='chromedriver.exe')
    driver.get(url)

    time.sleep(5)


    LOAD_MORE_BUTTON_XPATH = '//*[@id="buttons"]'
    count = 0
    while count < 55:
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="buttons"]'))).click()
            time.sleep(5)
            count += 1
        except Exception as e:
            print (e)
            count += 1
            break
        print(count)
    print ("Complete")
    time.sleep(5)

    main_art = driver.find_element_by_class_name('impr-content').find_element_by_xpath('.//h1').text

    print(f"{'-'*80}\nMain Article:\n{'-'*80}\n{main_art}\n{'-'*80}\nOther Articles:")

    articles = driver.find_elements_by_class_name('article-content')
    titles = []
    for article in articles:
        titles.append(article.find_element_by_xpath('.//h3').text)

    articles = driver.find_elements_by_class_name('image')
    count = -1
    with open('cms_scrape.csv', 'a', encoding='utf-8',newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        
        for article in articles:
            count += 1
            # print('-'*80)
            lnks = (article.find_elements_by_tag_name("a"))
            lnk = (lnks[0].get_attribute("href"))
            category = (lnks[1].get_attribute("href")).split('/')
            category = category[-1].strip()
            if category == 'This!':
                continue
            new_cat = category.replace('%20',' ')
            date = article.find_element_by_class_name('article-date')
            thuss = date.get_attribute('innerHTML')
            csv_writer.writerow([titles[count], new_cat, thuss, lnk])


    driver.quit()
