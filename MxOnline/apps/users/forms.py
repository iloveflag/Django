# _*_ encoding:utf-8 _*_
__author__ = 'zmbxzrq@outlook.com'
__date__ = '2019/2/11 16:53'
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
