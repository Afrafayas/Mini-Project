from django.conf.urls import url
from forum import views
urlpatterns=[
    url('pforum/',views.forum),
    url('vforum/',views.vforum),
    url('vforumu/',views.vforumu)

]