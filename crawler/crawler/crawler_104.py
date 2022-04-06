from bs4 import BeautifulSoup

import requests
import time
import re

     
start_time = time.time()  # timer

# url_104 = "https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=python%20django&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001000&order=15&asc=0&page=1&jobexp=1%2C3&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"
# response_html = requests.get(url_104).text
# bs4_obj = BeautifulSoup( response_html ,"lxml")

# opt = bs4_obj.find_all("option")
    
# ## get the last page number
# last_page_list=[]
# for i in opt:
#     if i.find(text=re.compile("第")):
#         opt_text= i.get_text()
#         opt_list = list(opt_text)
#         last_page_list.append(opt_list)
# last_page=int(len(last_page_list)/2)+1



# soup.find_all("a")   
# --> find_all returns a list
# --> scans the entire document looking for results
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# find() just returns the result.
# If find_all() can’t find anything, it returns an empty list. If find() can’t find anything, it returns None:


keyword_104 = "python"
endPage = 5

for page in range(1,endPage):
    url_104 = f"https://www.104.com.tw/jobs/search/?ro=0&keyword={keyword_104}&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001000&order=14&asc=0&page={page}&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"
    response_html = requests.get(url_104).text
    bs4_obj = BeautifulSoup(response_html ,"lxml")
    main_blocks = bs4_obj.find_all("div", {"class": "b-block__left"})  
    # sub_blocks = bs4_obj.find_all("div", {"class": "b-block__right b-pos-relative"})
    
    for block in main_blocks:
        url_compData = f"https://www.104.com.tw/jobs/search/?ro=0&keyword={keyword_104}&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001000&order=14&asc=0&page={page}&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"
        response_html = requests.get(url_104).text
        # raw data
        jobName_raw = block.find("a", {"class": "js-job-link"}) 
        company_raw = block.find_all("li")[1] # can't find by keyword, so find_all then choose.
        salary_raw = block.find("span", {"class": "b-tag--default"})
        discription_raw = block.find("p", {"class": "job-list-item__info b-clearfix b-content"})
        # applicantNum_raw = block.find("p", {"class": "job-list-item__info b-clearfix b-content"})
        updateDate_raw = block.find("span", {"class": "b-tit__date"})
        # classified data
        if jobName_raw is None:   # preventing "AttributeError: 'NoneType' object has no attribute 'getText'"
                continue
        jobName = jobName_raw.getText()
        company = company_raw.getText().strip()  
        salary = salary_raw.getText()
        updateDate = updateDate_raw.getText().strip() 
        # discription = discription_raw.getText().replace("\n", " ")
        result= [jobName, company, salary, updateDate]
        print(result)
             
        # if jobName.getText():
        #     print(result)
        # else:
        #     break
        # if job_name.getText():
        #     print(result)
        # else:
        #     break
        # print(result)

# print("Cost：" + str(time.time() - start_time) + "s")