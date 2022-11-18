from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.models import Login


# Create your views here.
def login(request):
    if request.method == "POST":
        uname = request.POST.get("unm")
        passw = request.POST.get("psw")
        print(passw)
        if Login.objects.filter(username=uname, password=passw):
            obj = Login.objects.filter(username=uname, password=passw)
            tp = ""
            for ob in obj:
                tp = ob.type
                uid = ob.u_id
                if tp == "admin":
                    request.session["uid"] = uid
                    return HttpResponseRedirect('/temp/admintemp/')
                elif tp == "user":
                    request.session["uid"] = uid
                    return HttpResponseRedirect('/temp/usertemp/')
                elif tp == "moderator":
                    request.session["uid"] = uid
                    return HttpResponseRedirect('/temp/moderatortemp/')
        else:
            objlist = "Username or Password incorrect... Please try again...!"
            context = {
            'msg': objlist,
            }
            return render(request, 'login/login.html', context)
    return render(request,'login/login.html')


