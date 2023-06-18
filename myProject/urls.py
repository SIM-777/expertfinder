"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from myApp import views
from django.urls import re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    # path('search',views.search,name="search"),
    path('GetExperts',views.GetExperts,name="GetExperts"),
    path("expert",views.showExperts),
    path("login_user",views.login_user),
    path("login",views.redirectlogin,name="login"),
    path("showExperts",views.showExperts,name="showExperts"),
    path("redirectlogin",views.redirectlogin,name="redirectlogin"),
    path("save_result/<str:id>",views.save_result,name="save_result"),
    path("expert_bio",views.expert_bio,name="expert_bio"),
    path("navbar",views.navbar),
    #path("view_report/<str:name>/<str:affiliations>",views.view_report,name="view_report"),
    re_path(r'^view_report/(?P<name>[\w\s]+)/(?P<affiliations>.+)/$', views.view_report, name='view_report'),

    
    path("manage_results",views.manage_results,name="manage_results"),
    path("delete_result/<str:id>",views.delete_result,name="delete_result"),
    path("search_experts_db",views.search_experts_from_db,name="search_experts_db"),
    path("navbar",views.navbar),
    path('search',views.search_for_experts,name="search"),
    path("logout_user",views.logout_user,name="logout_user")
    ]