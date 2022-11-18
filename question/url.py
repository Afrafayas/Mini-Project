from django.conf.urls import url
from question import views
urlpatterns=[
    url('pquestion/',views.question),
    url('mng/',views.mngq),
    url('vaq/',views.vquestion),
    url('quesapp/(?P<idd>\w+)',views.vapproved,name='quesapp'),
    url('quesrej/(?P<idd>\w+)',views.vrejected,name='quesrej'),

]
