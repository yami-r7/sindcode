from django.urls import path
from noticias.views import index, autores

urlpatterns = [
    path('',index),
    path('autor/',autores)
]