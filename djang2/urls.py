"""
URL configuration for djang2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

from app01 import views, account, task, order, chart, upload, city

urlpatterns = [
    # path("admin/", admin.site.urls),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    path('tt/', chart.tt),

    path("depart/list/",views.depart_list),
    path("depart/add/", views.depart_add),
    path("depart/delete/", views.depart_delete),
    path("depart/<int:nid>/edit/", views.depart_edit),
    path("depart/multi/", views.depart_multi),

    path("user/list/", views.user_list),
    path("user/add/", views.user_add),
    path("user/model/form/add/", views.user_model_form_add),
    path("user/delete/", views.user_delete),
    path("user/<int:id>/edit/", views.user_edit),

    path("lh/list/", views.lh_list),
    path("lh/add/", views.lh_add),
    path("lh/<int:id>/edit/", views.lh_edit),
    path("lh/delete/", views.lh_delete),

    path("admin/list/",views.admin_list),
    path("admin/add/",views.admin_add),
    path("admin/<int:id>/edit/", views.admin_edit),
    path("admin/delete/", views.admin_delete),
    path("admin/<int:id>/reset/", views.admin_reset),

    path('login/', account.login),
    path('image/code/', account.image_code),

    path('task/list/', task.task_list),
    path('task/ajax/', task.task_ajax),
    path('task/add/', task.task_add),

    path('order/list/', order.order_list),
    path('order/add/', order.order_add),
    path('order/delete/', order.order_delete),
    path('order/detail/', order.order_detail),
    path('order/edit/', order.order_edit),

    path('chart/list/', chart.chart_list),
    path('chart/bar/', chart.chart_bar),

    # 上传文件
    path('upload/list/', upload.upload_list),
    path('upload/form/', upload.upload_form),
    path('upload/modal/form/', upload.upload_modal_form),

    path('city/list/', city.city_list),
    path('city/add/', city.city_add),

]
