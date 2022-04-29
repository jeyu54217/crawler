from bs4 import BeautifulSoup
from selenium import webdriver
from pathlib import Path
import time

start_time = time.time()  # timer
chrome_path = f"{Path(__file__).resolve().parent}\chromedriver.exe"

def get_end_page(search_keyword):
    # Get html data by Selenium
    url_104 = f"https://www.104.com.tw/company/?keyword={search_keyword}&jobsource=checkc&mode=s"
    browser = webdriver.Chrome(chrome_path,)
    browser.get(url_104)
    _html_data = browser.page_source
    browser.close()
    # Get the end page number by bs4
    bs4_obj = BeautifulSoup(_html_data, 'lxml')
    all_page_list = bs4_obj.find_all("li", {"class":"multiselect__element position-relative"})  
    page_list = []
    for page in all_page_list:
        page_list.append(page.find('span', {"class":"multiselect__option d-flex align-items-center"}))
    end_page_num = len(page_list)-2
    return end_page_num

def get_html_data(search_keyword,end_page_num):
    # Get html data by Selenium
    url_104 = f"https://www.104.com.tw/company/?keyword={search_keyword}&jobsource=checkc&mode=s"
    browser = webdriver.Chrome(chrome_path,)
    browser.get(url_104)
    # auto-scrolling to the end page with AJAX
    starting_page = 1
    for starting_page in range(starting_page, end_page_num):
        browser.execute_script("window.scrollTo(100,document.body.scrollHeight)") 
        time.sleep(1)
    html_data = browser.page_source  # return a string
    browser.close()
    return html_data

def get_company_name(html_data):
    bs4_obj = BeautifulSoup(html_data, 'lxml')
    company_name_blocks = bs4_obj.find_all("div", {"class":"info-job text-break mb-2"})  # return a list
    company_names = []
    for name in company_name_blocks:
        name.find('a', {"data-gtm-list":"公司名稱"})
        company_names.append(name.getText().strip())
    return company_names

def get_company_intro(html_data):
    bs4_obj = BeautifulSoup(html_data, 'lxml')
    company_intro_blocks = bs4_obj.find_all("div", {"class":"info-container"})  # return a list
    company_intros = []
    for intro in company_intro_blocks:
        intro.find("div", {"class":"info-description text-gray-darker t4 text-break mb-2 position-relative info-description__line2"})
        company_intros.append(intro.getText().replace('\n',""))
    return company_intros

def get_check_page_url(html_data):
    bs4_obj = BeautifulSoup(html_data, 'lxml')
    check_page_url_blocks = bs4_obj.find_all("div", {"class":"info-job text-break mb-2"})
    check_page_urls  = []
    for block in check_page_url_blocks:
        for link in block:
            if link.get('href') is None:
                continue
            check_page_urls.append(
                f"https:{link.get('href').strip('').replace('?jobsource=checkc','')}"
                )
            # check_page_urls.append(link.get('href').strip("").strip("//"))
    return check_page_urls  

def get_company_id(html_data):
    bs4_obj = BeautifulSoup(html_data, 'lxml')
    company_id_blocks = bs4_obj.find_all("div", {"class":"info-job text-break mb-2"})
    company_id  = []
    for block in company_id_blocks:
        for id in block:
            if id.get('href') is None:
                continue
            company_id.append(
                id.get('href').replace('//www.104.com.tw/company/','').replace('?jobsource=checkc','').strip('')
                )
            # check_page_urls.append(link.get('href').strip("").strip("//"))
    return company_id
      
def get_company_product(check_page_urls):
    company_products = []
    for url in check_page_urls:
        # Get html data by Selenium
        browser = webdriver.Chrome(chrome_path,)
        browser.get(url)
        time.sleep(.5)
        _html_data = browser.page_source
        browser.close()
        # Get products' info by bs4
        bs4_obj = BeautifulSoup(_html_data, 'lxml')
        company_product_blocks = bs4_obj.find_all("div", {"id":"serve"})
        for product in company_product_blocks:
            product.find("p", {"class":"r3 mb-0 text-break"})
            # if product is None:
            #     return ""
            company_products.append(product.getText().replace('\r',"").replace('\n'," "))
    return company_products

# [issue] get_company_product doesn't match company name , try keyword : CTBC


if __name__ == '__main__':
    # company_info(0)
    # Workflow_control= sys.argv[1]
    # PATH_contorl    = sys.argv[2]
    # CONFIG_PATH     = sys.argv[3] 
    # Main(CONFIG_PATH,Workflow_control,PATH_contorl)

    search_keyword = "CTBC"
    end_page_num = get_end_page(search_keyword)
    html_data = get_html_data(search_keyword,end_page_num)
    # check_page_urls = get_check_page_url(html_data)
    company_name = get_company_name(html_data)
    # company_intro = get_company_intro(html_data)
    # company_product = get_company_product(check_page_urls)
    # company_id = get_company_id(html_data)
    print(company_name,len(company_name))
    # # print(check_page_urls,len(check_page_urls))
    # # print(company_intro,len(company_intro))
    # print(company_product,len(company_product))
    # # print(company_id,len(company_id))

print("Cost：" + str(time.time() - start_time) + " s")


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
        
        compData_url = f"https://twinc.com.tw/#/business/name/{company}/"
        compData_response = requests.get(compData_url).text
        compData_bs4Obj = BeautifulSoup(compData_response ,"lxml")
        print(compData_bs4Obj)
             
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