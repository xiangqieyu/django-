from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from django.shortcuts import render,redirect



class AuthMiddleware(MiddlewareMixin):

    def process_request(self,request):
        # 0.排除那些不需要登录就能访问的页面
        if request.path_info in ['/login/', '/image/code/']:
            return
        # 1.读取当前访问的用户的session信息，读到则继续
        info_dict = request.session.get("info")
        # print(info_dict)
        if info_dict:
            return
        return redirect('/login/')