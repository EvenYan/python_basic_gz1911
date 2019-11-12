from django.http import HttpResponse
from django.shortcuts import render
from my_app.models import AccountInfo

# Create your views here.


def index(request):
    return HttpResponse("Hello Django!")


def home(request):
    return render(request, 'index.html')


def save_account(request):
    username = request.POST.get("username")
    passwd = request.POST.get("passwd")
    phone_num = request.POST.get("phone_num")
    AccountInfo.objects.create(username=username, passwd=passwd, phone_num=phone_num)
    return HttpResponse("数据保存成功:%s" % username)