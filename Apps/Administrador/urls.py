from django.conf.urls import url, include
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^$', Login.as_view(), name="Login"),
    url(r'^salir/$', logout, name="salir", kwargs={'next_page': '/Administrador/'}),
    url(r'^Inicio/$', login_required(Inicio.as_view()), name='Inicio'),
    # < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - >
    url(r'^APersonas/$', login_required(AgregarPersona), name='APersonas'),
    url(r'^MPersonas/$', login_required(MostrarPersonas.as_view()), name='MPersonas'),
    url(r'^EPersonas/(?P<pk>\d+)$', login_required(EditPersonas.as_view()), name='EPersonas'),
    url(r'^ElPersonas/(?P<pk>\d+)$', login_required(ElimPersonas.as_view()), name='ElPersonas'),
    # < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - >
    url(r'^ATags/$', login_required(AgregarTags), name='ATags'),
    url(r'^MTags/$', login_required(MostrarTags.as_view()), name='MTags'),
    url(r'^ETags/(?P<pk>\d+)$', login_required(EditTags.as_view()), name='ETags'),
    url(r'^ElTags/(?P<pk>\d+)$', login_required(ElimTags.as_view()), name='ElTags'),
# < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - >
    url(r'^AImagenes/$', login_required(AgregarImagenes), name='AImagenes'),
    url(r'^MImagenes/$', login_required(MostrarImagenes.as_view()), name='MImagenes'),
    url(r'^EImagenes/(?P<pk>\d+)$', login_required(EditImagenes.as_view()), name='EImagenes'),
    url(r'^DImagenes/(?P<pk>\d+)$', login_required(DetalImagenes.as_view()), name='DImagenes'),
    url(r'^ElImagenes/(?P<pk>\d+)$', login_required(ElimImagenes.as_view()), name='ElImagenes'),
# < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - >
    url(r'^MImgTags/(?P<tag_id>[^/]+)/$', login_required(MostrarImgTag), name='MImgTags'),

]