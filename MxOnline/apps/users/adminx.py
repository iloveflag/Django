# _*_ encoding:utf-8 _*_
__author__ = 'zmbxzrq@outlook.com'
__date__ = '2019/2/1 11:09'

import xadmin

from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    pass


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
