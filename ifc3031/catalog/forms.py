from django import forms
from django.forms import ModelForm, ValidationError
from .models import Usuario, Nota
import datetime
from django.utils.translation import gettext as _
from django.utils.dateformat import DateFormat

class RenovarNotaForm(ModelForm):
    def clean_nota(self):
        data = self.cleaned_data['nota']

        # Verificar que la nota esté dentro del rango válido
        if data < 0 or data > 10:
            raise ValidationError(_('Nota inválida - debe estar entre 0 y 10'))

        return data
    
    nota = forms.FloatField(
        widget=forms.NumberInput(attrs={'step': '0.1'}),
        label=_('Nota'),
        help_text=_('Ingrese una nota entre 0 y 10.')
    )
    
    class Meta:
        model = Nota
        fields = ['nota',]
        labels = { 'nota': _('Nota'), }
        help_texts = { 'nota': _('Ingrese una nota válida.'), }

class UsuarioForm(forms.ModelForm):
    def clean_correo(self):
        data = self.cleaned_data['correo']

        if not data:
            raise ValidationError(_('El campo de correo es obligatorio'))
        return data

    correo = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Ingrese su correo'}),
        label=_('Correo'),
        help_text=_('Ingrese una dirección de correo válida.'),
        required=True,
    )
    
    class Meta:
        model = Usuario
        fields = '__all__'
