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



for page in range(1,100):
    url_104 = f"https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Django%20django&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001000&order=15&asc=0&page={page}&jobexp=1%2C3&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"
    response_html = requests.get(url_104).text

    bs4_obj = BeautifulSoup( response_html ,"lxml")  
    blocks = bs4_obj.find_all("div", {"class": "b-block__left"})  # main Job blocks

    for block in blocks:
        job = block.find("a", {"class": "js-job-link"})  
        if job is None:
                continue
        company = block.find_all("li")[1]  
        salary = block.find("span", {"class": "b-tag--default"})  
        
        result= [job.getText(),company.getText().strip(),salary.getText(),]
        if job.getText():
            print(result)
        else:
            break
     

print("Cost：" + str(time.time() - start_time) + "s")