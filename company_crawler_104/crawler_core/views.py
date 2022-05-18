from django.shortcuts import render, redirect
from .clawer_104_by_AJAX import *
from crawler_core.models import result_list
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import numpy as np

def home_page(request):
    return render(request,"search_page.html")
    # return render(request,"result_page.html")
    # return render(request,"selected_page.html")

@csrf_exempt
def main_crawler(request):
    if request.method =='POST':
        result_list.objects.all().delete() # important! reset DB before update or create
        keyword_list = list(request.POST.getlist('key_of_kwyword_list[]')[0].split(','))
        for keyword in keyword_list:
            if keyword == '':
                continue
            else:
                total_pages_num = get_total_pages(keyword)
                raw_data_list = get_json_data(keyword, total_pages_num)
                company_id_list = get_company_info(raw_data_list)[0]
                company_name_list = get_company_info(raw_data_list)[1]
                company_profile_list = get_company_info(raw_data_list)[2]
                company_product_list = get_company_product(company_id_list)
                # INSERT INTO DB
                for i in range(0, len(company_id_list)): # important!
                    id = company_id_list[i]
                    name = company_name_list[i]
                    profile = company_profile_list[i]
                    product = company_product_list[i]
                    result_list.objects.update_or_create(  # update or create but not do delete
                        company_id = id,
                        company_name = name,
                        company_profile = profile,
                        company_product = product,
                        )
    all_results = result_list.objects.all()
    context = {
            'result_list': all_results,
            }
    return render(request, "result_page.html", context) 

@csrf_exempt
def select_to_excel(request):
    if request.method =='POST':
        selected_id_list = list(request.POST.getlist('key_of_checked_list[]')[0].replace('checkbox_','').split(','))
        if selected_id_list == ['']:
            pass
        else:
            all_seleted_obj = result_list.objects.filter(company_id__in = selected_id_list)
            data = {
                'Name': [obj.company_name for obj in all_seleted_obj],
                'Profile': [obj.company_profile for obj in all_seleted_obj],
                'Product': [obj.company_product for obj in all_seleted_obj],
                'Note': [obj.user_note for obj in all_seleted_obj],
            }
            df = pd.DataFrame(data)
            df.to_excel('D:\\test.xlsx')
    return redirect('/')




