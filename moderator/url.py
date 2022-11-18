from django.conf.urls import url
from moderator import views

urlpatterns=[
    url('pmoderator/',views.moderator),
    url('viewmod/',views.vmoder),
    url('mup/(?P<idd>\w+)',views.mod_up,name='upd'),
    url('modelete/(?P<idd>\w+)',views.mod_del,name='dlt')

]
