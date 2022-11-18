from django.shortcuts import render
from moderator.models import Moderator
from login.models import Login

# Create your views here.
def moderator(request):
    if request.method=="POST":
        obj=Moderator()
        obj.moderator_name=request.POST.get('name')
        obj.age=request.POST.get('age')
        obj.qualification=request.POST.get('Quali')
        obj.email_id=request.POST.get('email')
        obj.category=request.POST.get('cat')
        obj.password=request.POST.get('pass')
        obj.save()

        ob = Login()
        ob.username = obj.moderator_name
        ob.password = obj.password
        ob.type = 'moderator'
        ob.u_id = obj.moderator_id
        ob.save()

    return render(request,'moderator/Moderator.html')



def vmoder(request):
    obj=Moderator.objects.all()
    context={
        'aa':obj
    }
    return render(request,'moderator/moderator_managmnt.html',context)

def mod_up(request,idd):
    obj=Moderator.objects.get(moderator_id=idd)
    context={
        'v':obj
    }
    if request.method=="POST":
        obj=Moderator.objects.get(moderator_id=idd)
        obj.moderator_name=request.POST.get('name')
        obj.age=request.POST.get('age')
        obj.qualification=request.POST.get('Quali')
        obj.email_id=request.POST.get('email')
        obj.category=request.POST.get('cat')
        obj.password=request.POST.get('pass')
        obj.save()
        return vmoder(request)
    return render(request,'moderator/updatem.html',context)

def mod_del(request,idd):
    obj=Moderator.objects.get(moderator_id=idd)
    obj.delete()
    return vmoder(request)



