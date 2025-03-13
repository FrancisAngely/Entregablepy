# catalog/views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Estudiante, Modulo, Nota, Usuario, Rol  # Ajustamos según los modelos

# Listado de estudiantes
class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'estudiantes/estudiante_list.html'

# Detalle de estudiante
class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = 'estudiantes/estudiante_detail.html'

# Crear estudiante
class EstudianteCreate(CreateView):
    model = Estudiante
    fields = ['first_name', 'last_name']  # Utilizamos first_name y last_name
    template_name = 'estudiantes/estudiante_form.html'

# Actualizar estudiante
class EstudianteUpdate(UpdateView):
    model = Estudiante
    fields = ['first_name', 'last_name']  # Utilizamos first_name y last_name
    template_name = 'estudiantes/estudiante_form.html'

# Eliminar estudiante
class EstudianteDelete(DeleteView):
    model = Estudiante
    template_name = 'estudiantes/estudiante_confirm_delete.html'
    success_url = reverse_lazy('estudiantes')

# Listado de módulos
class ModuloListView(ListView):
    model = Modulo
    template_name = 'modulos/modulo_list.html'

# Detalle de módulo
class ModuloDetailView(DetailView):
    model = Modulo
    template_name = 'modulos/modulo_detail.html'

# Crear módulo
class ModuloCreate(CreateView):
    model = Modulo
    fields = ['name']  # Ajustamos a 'name' del módulo
    template_name = 'modulos/modulo_form.html'

# Actualizar módulo
class ModuloUpdate(UpdateView):
    model = Modulo
    fields = ['name']  # Ajustamos a 'name' del módulo
    template_name = 'modulos/modulo_form.html'

# Eliminar módulo
class ModuloDelete(DeleteView):
    model = Modulo
    template_name = 'modulos/modulo_confirm_delete.html'
    success_url = reverse_lazy('modulos')

# Listado de usuarios
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/usuario_list.html'

# Detalle de usuario
class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'usuarios/usuario_detail.html'

# Crear usuario
class UsuarioCreate(CreateView):
    model = Usuario
    fields = ['email', 'first_name', 'last_name', 'role']  # Definimos los campos correspondientes
    template_name = 'usuarios/usuario_form.html'

# Actualizar usuario
class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = ['email', 'first_name', 'last_name', 'role']  # Definimos los campos correspondientes
    template_name = 'usuarios/usuario_form.html'

# Eliminar usuario
class UsuarioDelete(DeleteView):
    model = Usuario
    template_name = 'usuarios/usuario_confirm_delete.html'
    success_url = reverse_lazy('usuarios')

# Listado de roles
class RolListView(ListView):
    model = Rol
    template_name = 'roles/rol_list.html'

# Detalle de rol
class RolDetailView(DetailView):
    model = Rol
    template_name = 'roles/rol_detail.html'

# Crear rol
class RolCreate(CreateView):
    model = Rol
    fields = ['name']  # Definimos solo el nombre del rol
    template_name = 'roles/rol_form.html'

# Actualizar rol
class RolUpdate(UpdateView):
    model = Rol
    fields = ['name']  # Definimos solo el nombre del rol
    template_name = 'roles/rol_form.html'

# Eliminar rol
class RolDelete(DeleteView):
    model = Rol
    template_name = 'roles/rol_confirm_delete.html'
    success_url = reverse_lazy('roles')

# Listado de notas
class NotaListView(ListView):
    model = Nota
    template_name = 'notas/nota_list.html'

# Detalle de nota
class NotaDetailView(DetailView):
    model = Nota
    template_name = 'notas/nota_detail.html'

# Crear nota
class NotaCreate(CreateView):
    model = Nota
    fields = ['student', 'module', 'grade']  # Definimos los campos correspondientes
    template_name = 'notas/nota_form.html'

# Actualizar nota
class NotaUpdate(UpdateView):
    model = Nota
    fields = ['student', 'module', 'grade']  # Definimos los campos correspondientes
    template_name = 'notas/nota_form.html'

# Eliminar nota
class NotaDelete(DeleteView):
    model = Nota
    template_name = 'notas/nota_confirm_delete.html'
    success_url = reverse_lazy('notas')

from django.shortcuts import render

def index(request):
    return render(request, 'index.html') 