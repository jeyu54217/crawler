from django.conf.urls import include, url
from django.contrib import admin
from crawler_core import views as core_view

urlpatterns = [
    url(r'^$', core_view.home_page, name ='home_page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', core_view.main_crawler, name ='search'),
    url(r'^selected/', core_view.select_to_excel, name ='selected'),
]
