from django.conf.urls import include, url
from django.contrib import admin
from crawler_core import views as core_view

urlpatterns = [
    # Examples:
    url(r'^$', core_view.home_page, name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^search/', core_view.main_crawler,name='search'),

    url(r'^admin/', include(admin.site.urls)),
]


# from django.contrib import admin
# from django.conf.urls import path
# from crawler_core import views as core_view

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', core_view.home_page),
#     path('/?search_=<slug:slug>/', core_view.main_crawler),
#     # path('results/', views.main_crawler),
# ]

