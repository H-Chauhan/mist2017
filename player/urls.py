from django.conf.urls import url
from player import views

urlpatterns = [
    url(r'create/', views.createPlayer, name='create'),
]