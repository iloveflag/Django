# _*_ encoding:utf-8 _*_
from django.shortcuts import render
"""user登入的库"""
from django.contrib.auth import authenticate, login
"""自定义登录的库"""
from django.contrib.auth.backends import ModelBackend
"""用于选择or 或者and"""
from django.db.models import Q
"""class的方法去登录"""
from django.views.generic.base import View

from .models import UserProfile
from .forms import LoginForm
# Create your views here.
# 弱智的自定义登录class:
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return  None

"""基于类的登录方式"""
class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")  # type: object
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return  render(request, "index.html")
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误! "})
        else:
            return render(request, "login.html", {"login_form": login_form})
# 基于函数的登录方式,不建议采纳
# def user_login(request):
#     if request.method == "POST":
#         user_name = request.POST.get("username", "")  # type: object
#         pass_word = request.POST.get("password", "")
#         user = authenticate(username=user_name, password=pass_word)
#         if user is not None:
#             login(request, user)
#             return  render(request, "index.html")
#         else:
#             return render(request, "login.html", {"msg":"用户名或密码错误! "})
#     elif request.method == "GET":
#         return render(request, "login.html", {})