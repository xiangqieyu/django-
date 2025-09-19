from django.shortcuts import render, redirect
from django import forms
from app01.utils.bootstrap import BootStrapForm
from django.http import HttpResponse
from app01.utils.encrypt import md5
from app01 import models
from app01.utils.code import check_code

class LoginForm(BootStrapForm):
    username = forms.CharField(label="用户名", widget=forms.TextInput, required=True)
    password = forms.CharField(label="密码", widget=forms.PasswordInput, required=True)
    code = forms.CharField(label="验证码", widget=forms.TextInput, required=True)

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证成功，获取用户名和密码
        # print(form.cleaned_data)
        # 验证码的校验
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code', '')
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, 'login.html', {'form':  form})

        # 去数据库校验用户名和密码是否正确，获取用户对象
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()

        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {'form': form})
        # 用户名密码正确
        # 网站生成随机字符串，写道用户浏览器cookie中，再写入session中
        request.session["info"] = {'id': admin_object.id, 'name': admin_object.username}
        # session保存七天
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect("/admin/list/")
    return render(request, 'login.html', {'form': form})

from  io import BytesIO

def image_code(request):
    """生成图片验证码"""
    # # 调用pillow函数，生成图片
    # img, code_string = check_code()
    # print(code_string)
    # stream = BytesIO()
    # img.save(stream, 'png')
    # return HttpResponse(stream.getvalue())
    # 获取验证码图片和字符串
    img_data, code_string = check_code()

    # 存入session供后续验证
    request.session['image_code'] = code_string
    # 给session设置60s超时
    request.session.set_expiry(60)

    # 返回图片响应
    return HttpResponse(img_data, content_type='image/png')






