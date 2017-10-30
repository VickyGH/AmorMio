# coding=utf-8
from django.shortcuts import render, redirect, render_to_response
from django.views.generic import TemplateView, ListView, DetailView

from django.db.models import Q

from django.views.generic.edit import FormView, UpdateView, DeleteView, CreateView
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# Create your views here.
from Apps.Administrador.forms import *
from Apps.Administrador.models import *


class Inicio(TemplateView):
    template_name = 'Administrador/Inicio.html'
# < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > -
# Create your views here.
class Login(FormView):
    # Establecemos la plantilla a utilizar
    template_name = 'Registro/login.html'
    # Le indicamos que el formulario a utilizar es el formulario de autenticación de Django
    form_class = AuthenticationForm
    # Le decimos que cuando se haya completado exitosamente la operación nos redireccione a la url bienvenida de la aplicación personas
    success_url = reverse_lazy('Admin:Inicio')

    def dispatch(self, request, *args, **kwargs):
        # Si el usuario está autenticado entonces nos direcciona a la url establecida en success_url
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        # Sino lo está entonces nos muestra la plantilla del login simplemente
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

# < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > -
def AgregarPersona(request):
    if request.method == 'POST':
        form = AgregarPersonaForm(request.POST, request.FILES)
        if form.is_valid():
            newData = Personas(nombre = request.POST['nombre'],
                              apellidos = request.POST['apellidos'],
                              alias = request.POST['alias'],
                              foto = request.FILES['foto'])
            newData.save(form)
            return redirect("Admin:MPersonas")
    else:
        form = AgregarPersonaForm()
    return render(request, 'Administrador/Agregar.html', {'form':form , 'tipos':'Personas'})

class MostrarPersonas(ListView):
    template_name = 'Administrador/MPersonas.html'
    model = Personas
    paginate_by = 5

    def get_queryset(self):
        buscador = self.request.GET.get('search')
        queryset = Personas.objects.order_by('id')

        if buscador:
            queryset = queryset.filter(
                Q(nombre__icontains=buscador)|
				Q(apellidos__icontains=buscador)|
				Q(alias__icontains=buscador)
            )
        return queryset

class EditPersonas(UpdateView):
    template_name = 'Administrador/Agregar.html'
    model = Personas
    fields = ['nombre','apellidos','alias','foto']
    success_url = reverse_lazy('Admin:MPersonas')

class ElimPersonas(DeleteView):
    template_name = 'Administrador/Eliminar.html'
    model = Personas
    success_url = reverse_lazy('Admin:MPersonas')

# < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > -
def AgregarTags(request):
    if request.method == 'POST':
        form = AgregarTagsForm(request.POST)
        if form.is_valid():
            newData = Tags(nombre = request.POST['nombre'])
            newData.save(form)
            return redirect("Admin:MTags")
    else:
        form = AgregarTagsForm()
    return render(request, 'Administrador/Agregar.html', {'form':form, 'tipos':'Tags'})

class MostrarTags(ListView):
    template_name = 'Administrador/MTags.html'
    model = Tags
    paginate_by = 15

    def get_queryset(self):
        buscador = self.request.GET.get('search')
        queryset = Tags.objects.order_by('id')

        if buscador:
            queryset = queryset.filter(
                Q(nombre__icontains=buscador)
            )
        return queryset

class EditTags(UpdateView):
    template_name = 'Administrador/Agregar.html'
    model = Tags
    fields = ['nombre']
    success_url = reverse_lazy('Admin:MTags')

class ElimTags(DeleteView):
    template_name = 'Administrador/Eliminar.html'
    model = Tags
    success_url = reverse_lazy('Admin:MTags')

# < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > -
def AgregarImagenes(request):
    if request.method == 'POST':
        form = AgregarImagenesForm(request.POST, request.FILES)
        if form.is_valid():
            newData = Imagenes(imagen = request.FILES['imagen'],
                               #fechaCaptura = request.POST['fechaCaptura'],
                               personaUser = request.POST['personaUser'],
                               detalle = request.POST['detalle'])
            newData.save(form)
            newData.personasFoto.add(request.POST['personasFoto'])
            newData.tag.add(request.POST['tag'])

            return redirect("Admin:MImagenes")
    else:
        form = AgregarImagenesForm()
    return render(request, 'Administrador/Agregar.html', {'form':form, 'tipos':'Imagenes'})

class MostrarImagenes(ListView):
    template_name = 'Administrador/MImagenes.html'
    model = Imagenes
    paginate_by = 10

    def get_queryset(self):
        buscador = self.request.GET.get('search')
        queryset = Imagenes.objects.order_by('id')

        if buscador:
            queryset = queryset.filter(
                Q(detalle__icontains=buscador)
            )
        return queryset

class EditImagenes(UpdateView):
    template_name = 'Administrador/Agregar.html'
    model = Imagenes
    fields = ['imagen','fechaSubida','fechaCaptura','personasFoto','personaUser','detalle','tag']
    success_url = reverse_lazy('Admin:MImagenes')

class DetalImagenes(DetailView):
    template_name = 'Administrador/Detalles.html'
    model = Imagenes

class ElimImagenes(DeleteView):
    template_name = 'Administrador/Eliminar.html'
    model = Imagenes
    success_url = reverse_lazy('Admin:MImagenes')

# < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > - < - > -
# Buscador de Tags
def MostrarImgTag(request, tag_id):
    tag = Tags.objects.get(id=tag_id)
    img = Imagenes.objects.filter(tag=tag_id).order_by('id')

    return render(request, 'Administrador/MImagenes.html', {'object_list': img, 'Dato_Img':tag})








