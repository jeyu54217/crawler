# selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
    
# BeautifulSoup
import requests
from bs4 import BeautifulSoup
import re


url_104 ="https://www.104.com.tw/jobs/search/?ro=0&keyword=Django%20Python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001000&order=14&asc=0&page=1&jobexp=1%2C3&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"
# selenium

chrome = webdriver.Chrome('/home/jeyu54217/code/tt/chromedriver')
chrome.get(url_104)

# BeautifulSoup
# response_html = requests.get(url_104).text
# bs4_obj = BeautifulSoup( response_html , "lxml")
# bs4filter_by_name = bs4_obj.find_all("a",{"title":re.compile("公司名：.*")})


# selenium - select page


# def get_name(url,driver_path):
#     url_104 = str(url)
#     chrome = webdriver.Chrome()


bs4_obj_selenium = BeautifulSoup(chrome.page_source , "lxml")
selenium_opt = bs4_obj_selenium.find_all("option",{"value":"1"})
last_page_list=[]
for i in selenium_opt:
    if i.find(text=re.compile("第")):
        selenium_opt_text= i.get_text()
        selenium_opt_list = list(selenium_opt_text)
        last_page_list.append(selenium_opt_list)
        # >> [['第', ' ', '1', ' ', '/', ' ', 'X', ' ', '頁'], ['第', ' ', '1', ' ', '/', ' ', 'X', ' ', '頁']]
last_page= int(last_page_list[0][6])+1


num = 0
for page_num in range(3, last_page):
    select = Select(chrome.find_element_by_xpath("//select[@class='page-select js-paging-select gtm-paging-top']"))
    select_page = select.select_by_value(f"{page_num}")
    bs4_obj_selenium = BeautifulSoup(chrome.page_source , "lxml")
    bs4_filter_name = bs4_obj_selenium.find_all("a",{"title":re.compile("公司名：.*")})
    
    for name in bs4_filter_name:
        num = num+1
        company_name=name.get_text()
        print(
            f"{num}. {company_name}"
           )
    time.sleep(2)



# for x in range(0, 16):
#     chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(1)
    
# next_page_button=chrome.find_element_by_xpath("//option[@value='99']")
# if next_page_button:
#     next_page_button.click()


