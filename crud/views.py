from django.shortcuts import render
from django.http import HttpResponse
from crud.models import Member

# Create your views here.
def health(request):
    return HttpResponse("health check.")


def index(request):
    members = Member.objects.all().order_by("id")
    return render(request, "members/index.html", {"members": members})


def edit(request, id=None):
    return HttpResponse("編集")


def delete(request, id=None):
    return HttpResponse("削除")


def detail(request, id=None):
    return HttpResponse("詳細")
