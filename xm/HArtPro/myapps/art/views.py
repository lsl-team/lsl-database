from django.shortcuts import render

# Create your views here.
from art.models import Art
from user import helper


def show(request, id):
    # 阅读 art_id 的文章
    login_user = helper.getLoginInfo(request)  # 读取session登录的信息
    art = Art.objects.get(pk=id)

    return render(request, 'art/show.html', locals())