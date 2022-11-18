from django.shortcuts import render
from question.models import Question
from moderator.models import Moderator

# Create your views here.
def question(request):
    if request.method=="POST":
        obj=Question()
        obj.question=request.POST.get('qstns')
        obj.moderator_id="1"
        obj.category=request.POST.get('cat')
        obj.save()
    return render(request,'question/Question.html')

def vquestion(request):
    if request.method=='POST':
        vv=request.POST.get('pp')
        obj=Question.objects.filter(category__icontains=vv,status='Approved')
        context = {
            'x': obj
        }
        return render(request, 'question/view_approved_question.html', context)
    else:
        obj=Question.objects.filter(status='approved')
        context={
        'x': obj
        }
    return render(request,'question/view_approved_question.html',context)

def mngq(request):
    obj=Question.objects.all()
    context={
        'cc':obj
    }
    return render(request,'question/Qustion_management.html',context)


def vapproved(request,idd):
    obj = Question.objects.get(question_id=idd)
    obj.status = "Approved"
    obj.save()
    return mngq(request)
    #return render(request,'question/Qustion_management.html')

def vrejected(request,idd):
    obj = Question.objects.f(question_id=idd)
    obj.status = "Rejected"
    obj.save()
    return mngq(request)

    #return render(request,'question/view_approved_question.html')


