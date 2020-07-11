"""Mysearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path,re_path
from myapp import views
# import haystack.urls
urlpatterns = [
    url('admin/', admin.site.urls),
    url('test',views.test,name='test'),
    url(r'^$',views.initial,name='initial'),
    # path('^map/(. (dot))*8/$',views.map,name='map'),
    path('subject1/<str:sub>',views.subject1,name='subject1'),
    path('subject2/<str:index>',views.subject2,name='subject2'),#用Django路由匹配学科发展趋势里的词，生成对应二级学科的图
    path('directions/<str:kw>',views.dirction,name='directions'),#用Django路由匹配3D词云里的词，生成对应方向的图
    path('direction',views.search_dr,name='direction'),
    path('school/<str:name>',views.school,name='school'),
    path('index',views.index,name='index'),
    path('location',views.location,name='location'),
    url('search',views.search,name='search'),
    url('base',views.base,name='base'),
    url('sort',views.sortData,name='sort'),
    # url('search',include('haystack.urls')),
    url('myechart',views.myerchart,name='myechart'),

]
