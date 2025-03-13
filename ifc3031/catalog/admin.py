from django.contrib import admin

# Importar los modelos adaptados a la base de datos
from .models import Rol, Usuario, Estudiante, Modulo, Nota  # Nombres en español

# Registrar modelos en el admin
@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creado_en', 'actualizado_en')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'correo', 'primer_nombre', 'apellido', 'rol', 'creado_en', 'actualizado_en')
    list_filter = ('rol',)
    search_fields = ('correo', 'primer_nombre', 'apellido')

# admin.py
from django.contrib import admin
from .models import Estudiante

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('primer_nombre', 'apellido', 'creado_en', 'actualizado_en')
    list_filter = ('creado_en', 'actualizado_en')

admin.site.register(Estudiante, EstudianteAdmin)


@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creado_en', 'actualizado_en')
    search_fields = ('nombre',)

# admin.py
from django.contrib import admin
from .models import Nota

class NotaAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'modulo', 'nota', 'creado_en', 'actualizado_en')
    list_filter = ('modulo', 'nota')

admin.site.register(Nota, NotaAdmin)

