from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
#. is used since views for using in this urls.py is available in the same folder else
# folder name should be used
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.all_blogs,name="all_blogs"),
    path('<int:blog_id>/',views.detail,name="detail")
    
]
