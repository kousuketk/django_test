from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView

from crud.models import Member
from crud.forms import MemberForm

# Create your views here.
def health(request):
    return HttpResponse("health check.")


def index(request):
    members = Member.objects.all().order_by("id")
    return render(request, "members/index.html", {"members": members})


class MemberList(ListView):
    model = Member
    context_object_name = "members"
    template_name = "members/index.html"
    paginate_by = 1


def edit(request, id=None):
    if id:
        member = get_object_or_404(Member, pk=id)
    else:
        member = Member()

    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            member = form.save(commit=False)
            member.save()
            return redirect("index")
    else:
        form = MemberForm(instance=member)
    return render(request, "members/edit.html", dict(form=form, id=id))


def delete(request, id):
    member = get_object_or_404(Member, pk=id)
    member.delete()
    return redirect("index")


def detail(request, id=id):
    member = get_object_or_404(Member, pk=id)
    return render(request, "members/detail.html", {"member": member})
