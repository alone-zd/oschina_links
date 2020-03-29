from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from Apps.models import OsChina
# Create your views here.


def index(req):
    list = OsChina.objects.all()
    #分页
    paginator = Paginator(list, 20)
    # 得到用户点击的第几页，默认为1
    page_number = req.GET.get('page', 1)
    # 得到分页后的总页码数
    page = paginator.get_page(page_number)

    return render(req, 'index.html', context={'page': page})
