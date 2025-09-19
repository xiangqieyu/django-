from django.shortcuts import render
from django.http import JsonResponse

def chart_list(request):
    """数据统计页面"""


    return render(request, 'chart_list.html')



def chart_bar(request):
    """构造柱状图的数据"""
    legend = ['香茄鱼1','香茄鱼2']
    series_list = [
        {
            "name": '香茄鱼1',
            "type": 'bar',
            "data": [5, 20, 36, 10, 10, 20]
        },
        {
            "name": '香茄鱼2',
            "type": 'bar',
            "data": [15, 10, 26, 30, 35, 5]
        }
    ]
    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月']

    result = {
        "status": True,
        "data": {
            "legend": legend,
            "series_list": series_list,
            "x_axis": x_axis,
        }
    }
    return JsonResponse(result)


def tt(r):
    pass


