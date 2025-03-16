from django import forms
from django.forms import ModelForm, ValidationError
from django.utils.translation import gettext as _
from .models import Usuario, Nota, Estudiante

# 🔹 Formulario para Renovar Notas
class RenovarNotaForm(ModelForm):
    def clean_nota(self):
        data = self.cleaned_data.get('nota')

        # Verificar que la nota no sea None y esté dentro del rango válido
        if data is None:
            raise ValidationError(_('Este campo es obligatorio.'))
        if data < 0 or data > 10:
            raise ValidationError(_('Nota inválida - debe estar entre 0 y 10.'))

        return data
    
    nota = forms.FloatField(
        widget=forms.NumberInput(attrs={'step': '0.1', 'min': '0', 'max': '10'}),
        label=_('Nota'),
        help_text=_('Ingrese una nota entre 0 y 10.')
    )
    
    class Meta:
        model = Nota
        fields = ['nota']
        labels = {'nota': _('Nota')}
        help_texts = {'nota': _('Ingrese una nota válida.')}

# 🔹 Formulario para Usuario
class UsuarioForm(forms.ModelForm):
    def clean_correo(self):
        data = self.cleaned_data.get('correo')
        
        if not data:
            raise ValidationError(_('El campo de correo es obligatorio.'))

        if Usuario.objects.filter(correo=data).exists():
            raise ValidationError(_('Este correo ya está registrado.'))

        return data
    
    correo = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Ingrese su correo'}),
        label=_('Correo'),
        help_text=_('Ingrese una dirección de correo válida.'),
        required=True,
    )

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre'}),
        label=_('Nombre'),
        required=True,
        error_messages={'required': _('El nombre es obligatorio.')}
    )

    class Meta:
        model = Usuario
        fields = ['nombre', 'correo']  # Solo los campos esenciales
        labels = {
            'nombre': _('Nombre'),
            'correo': _('Correo Electrónico'),
        }
        help_texts = {
            'nombre': _('Ingrese su nombre completo.'),
            'correo': _('Ingrese un correo válido para el registro.'),
        }

# 🔹 Formulario para Estudiante
class EstudianteForm(forms.ModelForm):
    primer_nombre = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el primer nombre'}),
        label=_('Primer Nombre'),
        required=True,
        error_messages={'required': _('El primer nombre es obligatorio.')}
    )

    apellido = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el apellido'}),
        label=_('Apellido'),
        required=True,
        error_messages={'required': _('El apellido es obligatorio.')}
    )

    class Meta:
        model = Estudiante
        fields = ['primer_nombre', 'apellido']

    def clean(self):
        cleaned_data = super().clean()
        primer_nombre = cleaned_data.get('primer_nombre')
        apellido = cleaned_data.get('apellido')

        # Verificar si ya existe un estudiante con el mismo nombre y apellido
        if primer_nombre and apellido:
            if Estudiante.objects.filter(primer_nombre=primer_nombre, apellido=apellido).exists():
                raise forms.ValidationError("Ya existe un estudiante con ese nombre y apellido.")

        return cleaned_data
