# _*_ encoding:utf-8 _*_
from django.apps import AppConfig

# 后台左侧的名称:
class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = u"用户信息"
