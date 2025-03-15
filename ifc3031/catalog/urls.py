from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),

    # Rutas de Estudiantes
    path('', views.index, name='index'),  # Página de inicio
    path('estudiantes/', views.EstudianteListView.as_view(), name='estudiantes'),
    path('estudiante/<int:pk>/', views.EstudianteDetailView.as_view(), name='estudiante-detalle'),
    path('estudiante/crear/', views.EstudianteCreate.as_view(), name='estudiante-crear'),
    path('estudiante/<int:pk>/actualizar/', views.EstudianteUpdate.as_view(), name='estudiante-actualizar'),
    path('estudiante/<int:pk>/eliminar/', views.EstudianteDelete.as_view(), name='estudiante-eliminar'),

    # Rutas de Módulos
    path('modulos/', views.ModuloListView.as_view(), name='modulos'),
    path('modulo/<int:pk>/', views.ModuloDetailView.as_view(), name='modulo-detalle'),
    path('modulo/crear/', views.ModuloCreate.as_view(), name='modulo-crear'),
    path('modulo/<int:pk>/actualizar/', views.ModuloUpdate.as_view(), name='modulo-actualizar'),
    path('modulo/<int:pk>/eliminar/', views.ModuloDelete.as_view(), name='modulo-eliminar'),

    # Rutas de Notas
    path('notas/', views.NotaListView.as_view(), name='notas'),
    path('nota/<int:pk>/', views.NotaDetailView.as_view(), name='nota-detalle'),
    path('nota/crear/', views.NotaCreate.as_view(), name='nota-crear'),
    path('nota/<int:pk>/actualizar/', views.NotaUpdate.as_view(), name='nota-actualizar'),
    path('nota/<int:pk>/eliminar/', views.NotaDelete.as_view(), name='nota-eliminar'),

    # Rutas de Usuarios
    path('usuarios/', views.UsuarioListView.as_view(), name='usuarios'),
    path('usuario/<int:pk>/', views.UsuarioDetailView.as_view(), name='usuario-detalle'),
    path('usuario/crear/', views.UsuarioCreate.as_view(), name='usuario-crear'),
    path('usuario/<int:pk>/actualizar/', views.UsuarioUpdate.as_view(), name='usuario-actualizar'),
    path('usuario/<int:pk>/eliminar/', views.UsuarioDelete.as_view(), name='usuario-eliminar'),

    # Rutas de Roles
    path('roles/', views.RolListView.as_view(), name='roles'),
    path('rol/<int:pk>/', views.RolDetailView.as_view(), name='rol-detalle'),
    path('rol/crear/', views.RolCreate.as_view(), name='rol-crear'),
    path('rol/<int:pk>/actualizar/', views.RolUpdateView.as_view(), name='rol-actualizar'),
    path('rol/<int:pk>/eliminar/', views.RolDelete.as_view(), name='rol-eliminar'),
]
