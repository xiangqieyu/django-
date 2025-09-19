import json
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from django import forms
from app01.utils.Pagination import Pagination


class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"
        widgets = {
            # "detail": forms.Textarea,
            "detail": forms.TextInput
        }

def task_list(request):
    """任务列表"""
    queryset = models.Task.objects.all().order_by('-id')
    # 分页（与context结合,和task_list.html内
    #     <ul class="pagination">
    #         {{ page_string }}
    #     </ul>）
    page_object =  Pagination(request, queryset)

    form = TaskModelForm()
    context = {
        "form": form,
        "queryset": page_object.page_queryset, # 分完页的数据
        "page_string": page_object.html() # 生成页码
    }
    return render(request, "task_list.html", context)


@csrf_exempt
def task_ajax(request):
    print(request.GET)
    print(request.POST)

    data_dict = {"status": True, 'data': [11, 22, 33, 44]}
    return HttpResponse(json.dumps(data_dict))


@csrf_exempt
def task_add(request):
    print(request.POST, "request.POST")
    # 1.用户发送过来的数据进行校验（modelform进行校验）
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))

    data_dict = {"status": False, 'error': form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))