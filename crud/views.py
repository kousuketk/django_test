from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def health(request):
    return HttpResponse("health check.")


def index(request):
    return HttpResponse("一覧")


def edit(request, id=None):
    return HttpResponse("編集")


def delete(request, id=None):
    return HttpResponse("削除")


def detail(request, id=None):
    return HttpResponse("詳細")
