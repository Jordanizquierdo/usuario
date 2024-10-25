from django import forms
from .models import User
from django.core.exceptions import ValidationError

class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nombre', 'apellido', 'numero', 'correo', 'direccion', 'rut']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'minlength': 2, 'maxlength': 30}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'minlength': 2, 'maxlength': 30}),
            'numero': forms.TextInput(attrs={'class': 'form-control', 'pattern': r'^\d{9,10}$', 'title': 'El número debe tener entre 9 y 10 dígitos.'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'maxlength': 50}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'minlength': 5, 'maxlength': 30}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'pattern': r'^\d{1,8}-[0-9kK]{1}$', 'title': 'El RUT debe estar en el formato correcto (ej. 12345678-9).'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre and (len(nombre) < 2 or len(nombre) > 30):
            raise ValidationError("El nombre debe tener entre 2 y 30 caracteres.")
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if apellido and (len(apellido) < 2 or len(apellido) > 30):
            raise ValidationError("El apellido debe tener entre 2 y 30 caracteres.")
        return apellido


    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if correo and len(correo) > 30:
            raise ValidationError("El correo no debe exceder los 30 caracteres.")
        return correo

    def clean_direccion(self):
        direccion = self.cleaned_data.get('direccion')
        if direccion and (len(direccion) < 5 or len(direccion) > 30):
            raise ValidationError("La dirección debe tener entre 5 y 30 caracteres.")
        return direccion

    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        if not numero.isdigit() or not (9 <= len(numero) <= 10):
            raise ValidationError("El número debe contener entre 9 y 10 dígitos y solo números.")
        return numero

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if not rut or len(rut.split('-')) != 2:
            raise ValidationError("El RUT debe estar en el formato correcto (ej. 12345678-9).")
        return rut
