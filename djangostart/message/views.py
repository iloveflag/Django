#_*_ coding: utf-8 _*_
from django.shortcuts import render
from .models import UserMessage
# Create your views here.
def getform(request):

    # all_messages = UserMessage.objects.filter(name='bobby')  # type: object
    # for message in all_messages:
    #     print message.name
    # 读取数据

    # user_message = UserMessage()
    # user_message.name='zhaorenqun'
    # user_message.message='hello2'
    # user_message.address='上海'
    # user_message.email='2@2.com'
    # user_message.object_id='hello2'
    # user_message.save()
    # 保存数据

    # if request.method == 'POST':
    #     name = request.POST.get('name','')
    #     message=request.POST.get('message','')
    #     email = request.POST.get('email', '')
    #     address = request.POST.get('address', '')
    #     user_message = UserMessage()
    #     user_message.name=name
    #     user_message.message=message
    #     user_message.address=address
    #     user_message.email=email
    #     user_message.object_id='3test'
    #     user_message.save()
    #页面数据写入

    # all_messages = UserMessage.objects.filter(name='bobby',address='北京')  # type: object
    # # all_messages.delete() 删除1
    # for message in all_messages:
    #      message.delete()
    # #数据删除

    message=None
    all_messages = UserMessage.objects.filter(name='bobby')
    if all_messages:
        message=all_messages[0]
    return render(request, 'message_form.html',{
        "my_message":message
    })