from django.conf.urls import url
from passwordLog import views

urlpatterns = [
    url('video/',views.videoCreate,name='videocreate'),
]