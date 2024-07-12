from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from settings import CHROMEDRIVER_PATH
import pandas as pd

driver=webdriver.Chrome(CHROMEDRIVER_PATH)



full_data=pd.DataFrame(columns=['Company Name','Phone','Contact Person','Email','Website'])
rows=[]


for i in range(1,21):
    driver.get(f'https://aviationdirectory.biz/directory/?pp={i}')
    a_tags=driver.find_elements(By.CSS_SELECTOR,'#directory-listing-box a')
    links=[]
    for j in a_tags:
        links.append(j.get_attribute('href'))
    for link in links:

        driver.get(link)
        try:
            company_name=driver.find_element(By.CSS_SELECTOR,'.title').text
        except NoSuchElementException:
            company_name=''
        try:
            phone_number = driver.find_element(By.XPATH,"//div[strong[contains(text(),'Telephone:')]]").text

        except NoSuchElementException:
            try:
                phone_number=driver.find_element(By.XPATH,"//div[span[contains(text(),'TEL:')]]").text
            except:
                phone_number=''
        
        try:
            contact=driver.find_element(By.XPATH,"//h4[@class='left-listing-sub-title' and text()='EXECUTIVE INFO']/following-sibling::p").text
        except NoSuchElementException:
            contact=''
        try:
            email=driver.find_element(By.XPATH,"//*[contains(text(),'Email')]/following-sibling::a").text
        except NoSuchElementException:
            email=''
        try:
            website=driver.find_element(By.XPATH,"//*[contains(text(),'Website')]/following-sibling::a").text
        except NoSuchElementException:
            website=''

        data={
            'Company Name':company_name,
            'Phone':phone_number,
            'Contact Person':contact,
            'Email':email,
            'Website':website
        }                                                                                           

        rows.append(data)

# links=['https://aviationdirectory.biz/directory/vigor-precision-engineering-pte-ltd/', 'https://aviationdirectory.biz/directory/vigor-precision-engineering-pte-ltd/', 'https://aviationdirectory.biz/directory/viscoy-pte-ltd/', 'https://aviationdirectory.biz/directory/viscoy-pte-ltd/', 'https://aviationdirectory.biz/directory/visiontech-engineering-pte-ltd/', 'https://aviationdirectory.biz/directory/visiontech-engineering-pte-ltd/', 'https://aviationdirectory.biz/directory/voestalpine-additive-manufacturing-center-singapore-pte-ltd/', 'https://aviationdirectory.biz/directory/voestalpine-additive-manufacturing-center-singapore-pte-ltd/', 'https://aviationdirectory.biz/directory/voestalpine-specialty-metals-pte-ltd/', 'https://aviationdirectory.biz/directory/voestalpine-specialty-metals-pte-ltd/', 'https://aviationdirectory.biz/directory/volocopter/', 'https://aviationdirectory.biz/directory/volocopter/', 'https://aviationdirectory.biz/directory/wada-mold-industry-co-ltd/', 'https://aviationdirectory.biz/directory/wada-mold-industry-co-ltd/', 'https://aviationdirectory.biz/directory/wah-son-engineering-pte-ltd/', 'https://aviationdirectory.biz/directory/wah-son-engineering-pte-ltd/', 'https://aviationdirectory.biz/directory/walter-ag-singapore-pte-ltd/', 'https://aviationdirectory.biz/directory/walter-ag-singapore-pte-ltd/', 'https://aviationdirectory.biz/directory/walter-ag-singapore-pte-ltd/', 'https://aviationdirectory.biz/directory/watlow-singapore-pte-ltd/', 'https://aviationdirectory.biz/directory/watlow-singapore-pte-ltd/', 'https://aviationdirectory.biz/directory/weber-shandwick-worldwide-singapore-pte-ltd/', 'https://aviationdirectory.biz/directory/weber-shandwick-worldwide-singapore-pte-ltd/', 'https://aviationdirectory.biz/directory/wencor-llc/', 'https://aviationdirectory.biz/directory/wencor-llc/', 'https://aviationdirectory.biz/directory/werner-aero-services-asia-pacific-pte-ltd/', 'https://aviationdirectory.biz/directory/werner-aero-services-asia-pacific-pte-ltd/', 'https://aviationdirectory.biz/directory/we-the-flyers/', 'https://aviationdirectory.biz/directory/we-the-flyers/', 'https://aviationdirectory.biz/directory/white-case-pte-ltd/', 'https://aviationdirectory.biz/directory/white-case-pte-ltd/', 'https://aviationdirectory.biz/directory/whitefox-defense-technologies-inc/', 'https://aviationdirectory.biz/directory/whitefox-defense-technologies-inc/', 'https://aviationdirectory.biz/directory/winco-engineering-pte-ltd/', 'https://aviationdirectory.biz/directory/winco-engineering-pte-ltd/', 'https://aviationdirectory.biz/directory/windsor-airmotive-asia-pte-ltd/', 'https://aviationdirectory.biz/directory/windsor-airmotive-asia-pte-ltd/', 'https://aviationdirectory.biz/directory/windsor-airmotive-asia-pte-ltd/', 'https://aviationdirectory.biz/directory/wingsoverasia-pte-ltd/', 'https://aviationdirectory.biz/directory/wingsoverasia-pte-ltd/', 'https://aviationdirectory.biz/directory/wingspec-pte-ltd/', 'https://aviationdirectory.biz/directory/wingspec-pte-ltd/', 'https://aviationdirectory.biz/directory/witte-far-east-pte-ltd/', 'https://aviationdirectory.biz/directory/witte-far-east-pte-ltd/', 'https://aviationdirectory.biz/directory/wizlogix-pte-ltd/', 'https://aviationdirectory.biz/directory/wizlogix-pte-ltd/', 'https://aviationdirectory.biz/directory/wong-partnership-llp/', 'https://aviationdirectory.biz/directory/wong-partnership-llp/', 'https://aviationdirectory.biz/directory/workforce-singapore-agency/', 'https://aviationdirectory.biz/directory/workforce-singapore-agency/', 'https://aviationdirectory.biz/directory/xpac-technologies-pte-ltd/', 'https://aviationdirectory.biz/directory/xpac-technologies-pte-ltd/', 'https://aviationdirectory.biz/directory/xpo-logistics-worldwide-asia-pacific-pte-ltd/', 'https://aviationdirectory.biz/directory/xpo-logistics-worldwide-asia-pacific-pte-ltd/', 'https://aviationdirectory.biz/directory/yamaco-co-ltd/', 'https://aviationdirectory.biz/directory/yamaco-co-ltd/', 'https://aviationdirectory.biz/directory/yamato-gokin-co-ltd/', 'https://aviationdirectory.biz/directory/yamato-gokin-co-ltd/', 'https://aviationdirectory.biz/directory/yeonhab-precision-co-ltd/', 'https://aviationdirectory.biz/directory/yeonhab-precision-co-ltd/', 'https://aviationdirectory.biz/directory/yin-shan-engineering-pte-ltd/', 'https://aviationdirectory.biz/directory/yin-shan-engineering-pte-ltd/', 'https://aviationdirectory.biz/directory/yjp-surveyors-pte-ltd/', 'https://aviationdirectory.biz/directory/yjp-surveyors-pte-ltd/', 'https://aviationdirectory.biz/directory/ymc-forging-m-sdn-bhd/', 'https://aviationdirectory.biz/directory/ymc-forging-m-sdn-bhd/', 'https://aviationdirectory.biz/directory/yoshimasu-seisakusho-co-ltd/', 'https://aviationdirectory.biz/directory/yoshimasu-seisakusho-co-ltd/', 'https://aviationdirectory.biz/directory/yoshitomi-unyu-co-ltd/', 'https://aviationdirectory.biz/directory/yoshitomi-unyu-co-ltd/', 'https://aviationdirectory.biz/directory/youngpoong-electronics-co-ltd/', 'https://aviationdirectory.biz/directory/youngpoong-electronics-co-ltd/', 'https://aviationdirectory.biz/directory/yuki-precision-co-ltd/', 'https://aviationdirectory.biz/directory/yuki-precision-co-ltd/', 'https://aviationdirectory.biz/directory/yulkok-ltd/', 'https://aviationdirectory.biz/directory/yulkok-ltd/', 'https://aviationdirectory.biz/directory/yusen-logistics-singapore-pte-ltd/', 'https://aviationdirectory.biz/directory/yusen-logistics-singapore-pte-ltd/', 'https://aviationdirectory.biz/directory/?pp=19', 'https://aviationdirectory.biz/directory/', 'https://aviationdirectory.biz/directory/?pp=18', 'https://aviationdirectory.biz/directory/?pp=19']

# different_links=[]



full_data=pd.DataFrame(rows)

full_data.to_excel('updated_aviation_directory_data.xlsx',index=False)

