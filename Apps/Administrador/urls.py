from django.conf.urls import url, include
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^$', Login.as_view(), name="Login"),
    url(r'^salir/$', logout, name="salir", kwargs={'next_page': '/Administrador/'}),
    url(r'^Inicio/$', login_required(Inicio.as_view()), name='Inicio'),
]