from django.shortcuts import render
from forum.models import Forum
from moderator.models import Moderator
# Create your views here.
def forum(request):
    obj=Moderator.objects.all()
    context={
        'x':obj,
    }
    if request.method=="POST":
        obj=Forum()
        obj.forum_name=request.POST.get('name')
        obj.moderator_id=request.POST.get('mod')
        obj.save()
    return render(request,'forum/Forum.html',context)

def vforum(request):
    obj=Forum.objects.all()
    context={
        'x': obj
    }
    return render(request,'forum/view_forum_moder.html',context)


def vforumu(request):
    obj=Forum.objects.all()
    context={
        'y': obj
    }
    return render(request,'forum/view_forum_user.html',context)