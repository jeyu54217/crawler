# selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
    
# BeautifulSoup
from bs4 import BeautifulSoup
import re


def get_name():
    url = "https://www.104.com.tw/jobs/search/?ro=0&keyword=Django%20&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001000&order=1&asc=0&page=1&jobexp=1%2C3&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"
    # url = f"https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Django%20Python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001000&order=14&asc=0&page=1&jobexp=1%2C3&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"
    chrome = webdriver.Chrome('/home/jeyu54217/code/crawler/crawler/crawler/chromedriver')
    chrome.get(url)
    time.sleep(3)
    
    bs4_obj = BeautifulSoup(chrome.page_source , "lxml")
    selenium_opt = bs4_obj.find_all("option")
    
    ## get the last page number
    last_page_list=[]
    for i in selenium_opt:
        if i.find(text=re.compile("第")):
            opt_text= i.get_text()
            opt_list = list(opt_text)
            last_page_list.append(opt_list)
    last_page=int(len(last_page_list)/2)+1
    
    ## return company names
    # num = 0
    
    for page_num in range(2, last_page):
        find_option = Select(chrome.find_element_by_xpath("//select[@class='page-select js-paging-select gtm-paging-top']"))
        find_option.select_by_value(f"{page_num}")
        
        bs4_obj2 = BeautifulSoup(chrome.page_source , "lxml")
        filter_by_name = bs4_obj2.find_all("a",{"title":re.compile("公司名：.*")})
        company_name_list=[]
        company_name_list2=[]
        for name in filter_by_name:
            company_name=name.get_text()
            company_name_list.append(company_name)
            company_name_list2.append(company_name_list)

        time.sleep(2)
    c = sum(company_name_list2, [])
    print(company_name_list)
    
get_name()
# <a href="//www.104.com.tw/job/7bka6?jobsource=jolist_d_relevance" class="js-job-link" target="_blank" data-qa-id="jobSeachResultTitle">數據分析師(數據應用部)</a>
