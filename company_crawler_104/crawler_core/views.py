from django.shortcuts import render
from django.http import Http404
from .clawer_104_by_AJAX import *
from crawler_core.models import result_list, selected_list
# from .forms import FormQuery


def home_page(request):
    # return render(request,"result_page.html")
    return render(request,"search_page.html")
    # return render(request,"selected_page.html")

def main_crawler(request):
    total_pages_num = get_total_pages(keyword)
    raw_data_list = get_json_data(keyword, total_pages_num)

    company_id_list = get_company_info(raw_data_list)[0]
    company_name_list = get_company_info(raw_data_list)[1]
    company_profile_list = get_company_info(raw_data_list)[2]
    company_product_list = get_company_product(company_id_list)
    if request.method == 'POST':
        try:
            if len(company_id_list) == len(company_name_list) == len(company_profile_list) == len(company_product_list):
                for _index in range(0, len(company_id_list) + 1):
                    id = company_id_list[_index]
                    name = company_name_list[_index]
                    profile = company_profile_list[_index]
                    product = company_product_list[_index]
                    result_list.objects.update_or_create(id, name, profile, product)
                # for id in company_id_list:
                #     setattr(results, 'company_id', id)
                # for name in company_name_list:
                #     setattr(results, 'company_name', name)
                # for profile in company_profile_list:
                #     setattr(results, 'company_profile', profile)
                # for product in company_product_list:
                #     setattr(results, 'company_product', product)
                # results.save()
                context = {
                    'result_list': result_list.objects.all(),
                    }
                return render(request, "result_page.html", context)
            else:
                pass
        except:
            raise Http404("The crawler's culomn doesn't match, please try again")
  
def selected(request):
    '''
    1. get select_box info --> return True
    2. update DB 'result_list.user_selected'
    3. get DB if 'result_list.user_selected' == True
    4. save() got data to DB 'selected_list'
    5. get 'selected_list' 
    6. render 'selected_list'  to result_page.html
    '''
    context = {
        'selected_list': selected_list.objects.all(),
        }
    return render(request, "selected_page.html", context)
