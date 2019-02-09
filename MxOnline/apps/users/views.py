# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate, login
"""user登入的库"""
from django.contrib.auth.backends import ModelBackend
"""自定义登录的库"""
from django.db.models import Q
"""用于选择or 或者and"""
from .models import UserProfile
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


def user_login(request):
    if request.method == "POST":
        user_name = request.POST.get("username", "")  # type: object
        pass_word = request.POST.get("password", "")
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return  render(request, "index.html")
        else:
            return render(request, "login.html", {"msg":"用户名或密码错误! "})
    elif request.method == "GET":
        return render(request, "login.html", {})