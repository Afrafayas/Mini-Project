from django.conf.urls import url
from temp import views

urlpatterns=[
    url('hometemp/', views.home),
    url('admintemp/', views.admin),
    url('usertemp/', views.user),
    url('moderatortemp/', views.moderator)
]