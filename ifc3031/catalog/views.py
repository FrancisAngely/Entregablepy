# catalog/views.py

from django.contrib.auth.mixins import LoginRequiredMixin  # Importa LoginRequiredMixin
from django.contrib.auth.decorators import login_required  # Importa el decorador


from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.forms import EstudianteForm
from .models import Estudiante, Modulo, Nota, Usuario, Rol  # Ajustamos según los modelos
from django.contrib.auth.models import User


# Listado de roles
class RolListView(LoginRequiredMixin, ListView):
    model = Rol
    template_name = 'catalog/rol_list.html' 
    context_object_name = 'roles'  

# Detalle de rol
class RolDetailView(LoginRequiredMixin, DetailView):
    model = Rol
    template_name = 'catalog/rol_detail.html'

# Crear rol
class RolCreate(LoginRequiredMixin, CreateView):
    model = Rol
    fields = ['nombre']
    template_name = 'catalog/rol_form.html'
    success_url = reverse_lazy('roles')

# Actualizar rol
class RolUpdateView(LoginRequiredMixin, UpdateView):
    model = Rol
    fields = ['nombre']
    template_name = 'catalog/rol_update.html'
    success_url = reverse_lazy('roles') 

# Eliminar rol
class RolDelete(LoginRequiredMixin, DeleteView):
    model = Rol
    template_name = 'catalog/rol_confirm_delete.html'
    success_url = reverse_lazy('roles')

# Listado de usuarios
class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = 'catalog/usuario_list.html'

# Detalle de usuario
class UsuarioDetailView(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = 'catalog/usuario_detail.html'

# Crear usuario
class UsuarioCreate(LoginRequiredMixin, CreateView):
    model = Usuario
    template_name = 'catalog/usuario_form.html'
    fields = ['correo', 'primer_nombre', 'apellido', 'rol', 'password']

    success_url = reverse_lazy('usuarios')
    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.save()
        user = User.objects.create_user(
            username=usuario.correo,
            email=usuario.correo,
            password=usuario.password
        )
        user.first_name = usuario.primer_nombre
        user.last_name = usuario.apellido
        user.save()
        return super().form_valid(form)

# Actualizar usuario
class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ['correo', 'primer_nombre', 'apellido', 'rol', 'password']
    context_object_name = 'usuario' 
    template_name = 'catalog/usuario_update.html'
    def get_success_url(self):
        return reverse_lazy('usuarios')

# Eliminar usuario
class UsuarioDelete(LoginRequiredMixin, DeleteView):
    model = Usuario
    template_name = 'catalog/usuario_confirm_delete.html'
    success_url = reverse_lazy('usuarios')

# Listado de estudiantes
class EstudianteListView(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = 'catalog/estudiante_list.html'
    context_object_name = 'estudiantes'

# Detalle de estudiante
class EstudianteDetailView(LoginRequiredMixin, DetailView):
    model = Estudiante
    template_name = 'catalog/estudiante_detail.html'

# Crear estudiante
class EstudianteCreate(LoginRequiredMixin, CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'catalog/estudiante_form.html'
    success_url = reverse_lazy('estudiantes')

# Actualizar estudiante
class EstudianteUpdate(LoginRequiredMixin, UpdateView):
    model = Estudiante
    fields = ['primer_nombre', 'apellido']
    template_name = 'catalog/estudiante_update.html'

# Eliminar estudiante
class EstudianteDelete(LoginRequiredMixin, DeleteView):
    model = Estudiante
    template_name = 'catalog/estudiante_confirm_delete.html'
    success_url = reverse_lazy('estudiantes')

# Listado de módulos
class ModuloListView(LoginRequiredMixin, ListView):
    model = Modulo
    template_name = 'catalog/modulos_list.html'
    context_object_name = 'modulos'

# Detalle de módulo
class ModuloDetailView(LoginRequiredMixin, DetailView):
    model = Modulo
    template_name = 'catalog/modulos_detail.html'

# Crear módulo
class ModuloCreate(LoginRequiredMixin, CreateView):
    model = Modulo
    fields = ['nombre']
    template_name = 'catalog/modulos_form.html'
    success_url = reverse_lazy('modulos')

# Actualizar módulo
class ModuloUpdate(LoginRequiredMixin, UpdateView):
    model = Modulo
    fields = ['nombre']
    template_name = 'catalog/modulos_update.html'
    success_url = reverse_lazy('modulos')

# Eliminar módulo
class ModuloDelete(LoginRequiredMixin, DeleteView):
    model = Modulo
    template_name = 'catalog/modulos_confirm_delete.html'
    success_url = reverse_lazy('modulos')

# Listado de notas
class NotaListView(LoginRequiredMixin, ListView):
    model = Nota
    template_name = 'catalog/nota_list.html'

# Detalle de nota
class NotaDetailView(LoginRequiredMixin, DetailView):
    model = Nota
    template_name = 'catalog/nota_detail.html'

# Crear nota
class NotaCreate(LoginRequiredMixin, CreateView):
    model = Nota
    fields = ['estudiante', 'modulo', 'nota']
    template_name = 'catalog/nota_form.html'

# Actualizar nota
class NotaUpdate(LoginRequiredMixin, UpdateView):
    model = Nota
    fields = ['estudiante', 'modulo', 'nota']
    template_name = 'catalog/nota_update.html'

# Eliminar nota
class NotaDelete(LoginRequiredMixin, DeleteView):
    model = Nota
    template_name = 'catalog/nota_confirm_delete.html'
    success_url = reverse_lazy('notas')

# Vista principal de conteo de registros
from django.shortcuts import render
@login_required
def index(request):
    num_estudiantes = Estudiante.objects.count()
    num_usuarios = Usuario.objects.count()
    num_roles = Rol.objects.count()
    num_modulos = Modulo.objects.count()
    num_notas = Nota.objects.count()

    context = {
        'num_estudiantes': num_estudiantes,
        'num_usuarios': num_usuarios,
        'num_roles': num_roles,
        'num_modulos': num_modulos,
        'num_notas': num_notas
    }

    return render(request, 'index.html', context)
