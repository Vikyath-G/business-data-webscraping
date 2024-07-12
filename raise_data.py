from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from settings import CHROMEDRIVER_PATH
import pandas as pd

driver=webdriver.Chrome(CHROMEDRIVER_PATH)



full_data=pd.DataFrame(columns=['Company Name','Email','Website','Description','Products and Services'])
rows=[]


driver.get('https://www.raise.sg/directory/directories/default.html?')

page_elements=driver.find_elements(By.CSS_SELECTOR,'div.pagination li')
page_links=['https://www.raise.sg/directory/directories/default.html?']

for i in page_elements[1:]:
    a_tag=i.find_element(By.TAG_NAME,'a')
    page_links.append(a_tag.get_attribute('href'))



for page_link in page_links:
    driver.get(page_link)
    links=[]
    link_elements=driver.find_elements(By.CSS_SELECTOR,'div.infor-content a')
    for link_element in link_elements:
        links.append(link_element.get_attribute('href'))

    for link in links:
        driver.get(link)

        try:
            name=driver.find_element(By.TAG_NAME,'h3').text
        except:
            name=''
        try:
            email=driver.find_element(By.CSS_SELECTOR,'div.note a').text
        except:
            email=''
        try:
            website=driver.find_element(By.CSS_SELECTOR,'a.website').get_attribute('href')
        except:
            website=''
        try:
            social=driver.find_elements(By.CSS_SELECTOR,'div.pull-right.social a')
            instagram=social[1].get_attribute('href')
            facebook=social[0].get_attribute('href')
        except:
            instagram=''
            facebook=''
        try:
            intro=driver.find_elements(By.CSS_SELECTOR,'div.service div.intro')
            description=intro[0].text
            products_services=intro[1].text
        except:
            description=''
            products_services=''

        data={
            'Company Name':name,
            'Email':email,
            'website':website,
            'Description':description,
            'Products and Services':products_services
        }

        rows.append(data)

full_data=pd.DataFrame(rows)

full_data.to_excel('raise_business_data.xlsx',index=False)