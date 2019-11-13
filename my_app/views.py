from django.http import HttpResponse
from django.shortcuts import render
from my_app.models import AccountInfo
from my_app.tools import gen_secret

# Create your views here.


def index(request):
    return HttpResponse("Hello Django!")


def home(request):
    return render(request, 'index.html')


def save_account(request):
    username = request.POST.get("username")
    passwd = request.POST.get("passwd")
    passwd = gen_secret(passwd)
    phone_num = request.POST.get("phone_num")
    AccountInfo.objects.create(username=username, passwd=passwd, phone_num=phone_num)
    return HttpResponse("数据保存成功:%s" % username)


def contact(requset):
    contact_list = AccountInfo.objects.all()
    # 修改联系人列表中第二个人的姓名
    # contat = contact_list[2]
    # contat.username = "Iris"
    # contat.save()
    print(contact_list)
    c = {"contact_list": contact_list}
    return render(requset, 'contact_list.html', context=c)


def detail(request, id):
    contact = AccountInfo.objects.get(id=id)
    print(contact)
    return render(request, "detail.html", context={"contact": contact})