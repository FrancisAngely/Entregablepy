# catalog/views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.forms import EstudianteForm
from .models import Estudiante, Modulo, Nota, Usuario, Rol  # Ajustamos según los modelos

# Listado de roles
class RolListView(ListView):
    model = Rol
    template_name = 'catalog/rol_list.html' 
    context_object_name = 'roles'  

# Detalle de rol
class RolDetailView(DetailView):
    model = Rol
    template_name = 'catalog/rol_detail.html'

# Crear rol
class RolCreate(CreateView):
    model = Rol
    fields = ['nombre']  # Definimos solo el nombre del rol
    template_name = 'catalog/rol_form.html'
    success_url = reverse_lazy('roles')


# Actualizar rol
class RolUpdateView(UpdateView):
    model = Rol
    fields = ['nombre']  # Los campos que el usuario puede actualizar
    template_name = 'catalog/rol_update.html'  # Aquí se usa nuestra plantilla de formulario
    success_url = reverse_lazy('roles') 

# Eliminar rol
class RolDelete(DeleteView):
    model = Rol
    template_name = 'catalog/rol_confirm_delete.html'
    success_url = reverse_lazy('roles')

# Listado de usuarios
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'catalog/usuario_list.html'

# Detalle de usuario
class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'catalog/usuario_detail.html'

# Crear usuario
class UsuarioCreate(CreateView):
    model = Usuario
    template_name = 'catalog/usuario_form.html'  # Verifica que este nombre de plantilla sea correcto
    fields = ['correo', 'primer_nombre', 'apellido', 'rol', 'password']
    success_url = reverse_lazy('usuarios')

# Actualizar usuario
class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = ['correo', 'primer_nombre', 'apellido', 'rol', 'password']  # Campos a incluir en el formulario
    context_object_name = 'usuario' 
    template_name = 'catalog/usuario_update.html'
    def get_success_url(self):
        return reverse_lazy('usuarios') # Redirigir a la lista de usuarios

# Eliminar usuario
class UsuarioDelete(DeleteView):
    model = Usuario
    template_name = 'catalog/usuario_confirm_delete.html'
    success_url = reverse_lazy('usuarios')

# Listado de estudiantes
class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'catalog/estudiante_list.html'
    context_object_name = 'estudiantes'  # Cambiamos el nombre del contexto


# Detalle de estudiante
class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = 'catalog/estudiante_detail.html'

# Crear estudiante
class EstudianteCreate(CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'catalog/estudiante_form.html'
    success_url = reverse_lazy('estudiantes') 

# Actualizar estudiante
class EstudianteUpdate(UpdateView):
    model = Estudiante
    fields = ['primer_nombre', 'apellido']  # Agrega los campos que deseas actualizar
    template_name = 'catalog/estudiante_update.html'

# Eliminar estudiante
class EstudianteDelete(DeleteView):
    model = Estudiante
    template_name = 'catalog/estudiante_confirm_delete.html'
    success_url = reverse_lazy('estudiantes')

# Listado de módulos
class ModuloListView(ListView):
    model = Modulo
    template_name = 'catalog/modulos_list.html'
    context_object_name = 'modulos'  # Cambiamos el nombre del contexto

# Detalle de módulo
class ModuloDetailView(DetailView):
    model = Modulo
    template_name = 'catalog/modulos_detail.html'


# Crear módulo
class ModuloCreate(CreateView):
    model = Modulo
    fields = ['nombre']  # Ajustamos a 'name' del módulo
    template_name = 'catalog/modulos_form.html'  # Nombre corregido
    success_url = reverse_lazy('modulos')  # Redirige a la lista de módulos después de crear uno

# Actualizar módulo
class ModuloUpdate(UpdateView):
    model = Modulo
    fields = ['nombre']  # Ajustamos a 'name' del módulo
    template_name = 'catalog/modulos_update.html'
    success_url = reverse_lazy('modulos')  # Redirigir a la lista de módulos después de actualizar

# Eliminar módulo
class ModuloDelete(DeleteView):
    model = Modulo
    template_name = 'catalog/modulos_confirm_delete.html'
    success_url = reverse_lazy('modulos')  # Redirigir a la lista de módulos después de eliminar


# Listado de notas
class NotaListView(ListView):
    model = Nota
    template_name = 'catalog/nota_list.html'

# Detalle de nota
class NotaDetailView(DetailView):
    model = Nota
    template_name = 'catalog/nota_detail.html'

# Crear nota
class NotaCreate(CreateView):
    model = Nota
    fields = ['student', 'module', 'grade']  # Definimos los campos correspondientes
    template_name = 'catalog/nota_form.html'

# Actualizar nota
class NotaUpdate(UpdateView):
    model = Nota
    fields = ['student', 'module', 'grade']  # Definimos los campos correspondientes
    template_name = 'catalog/nota_update.html'

# Eliminar nota
class NotaDelete(DeleteView):
    model = Nota
    template_name = 'catalog/nota_confirm_delete.html'
    success_url = reverse_lazy('notas')

from django.shortcuts import render

def index(request):
    # Obtener el conteo de cada tipo de registro
    num_estudiantes = Estudiante.objects.count()
    num_usuarios = Usuario.objects.count()
    num_roles = Rol.objects.count()
    num_modulos = Modulo.objects.count()
    num_notas = Nota.objects.count()

    # Pasar los datos al contexto de la plantilla
    context = {
        'num_estudiantes': num_estudiantes,
        'num_usuarios': num_usuarios,
        'num_roles': num_roles,
        'num_modulos': num_modulos,
        'num_notas': num_notas
    }

    return render(request, 'index.html', context)

