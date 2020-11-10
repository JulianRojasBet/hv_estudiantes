from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.models import Usuario, Oferta


class SignUpForm(UserCreationForm):
    documento = forms.CharField(max_length=15, )
    nombre = forms.CharField(max_length=70)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=13, required=False, help_text='Opcional')
    direccion = forms.CharField(max_length=50, required=False, help_text='Opcional')
    fecha_nacimiento = forms.DateField(required=False, help_text='Opcional')
    sexo = forms.CharField(max_length=10, required=False, help_text='Opcional')
    nacionalidad = forms.CharField(max_length=30, required=False, help_text='Opcional')
    tipo = forms.CharField(max_length=15, required=False, help_text='Opcional')
    categoria = forms.CharField(max_length=15, required=False, help_text='Opcional')

    class Meta:
        model = Usuario
        fields = ('username', 'password1', 'password2', 'documento', 'nombre', 'email', 'telefono', 'direccion',
                  'fecha_nacimiento', 'sexo', 'nacionalidad', 'tipo', 'categoria')

class SignUpOfferForm(UserCreationForm):
    documento = forms.CharField(max_length=15, )
    nombre = forms.CharField(max_length=70)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=13, required=True)

    class Meta:
        model = Usuario
        fields = ('username', 'password1', 'password2', 'documento', 'nombre', 'email', 'telefono')

class AddNewOfferForm(forms.Form):
    nombre = forms.CharField(max_length=15)
    fecha_limite = forms.DateTimeField() # Default
    info_empresa = forms.CharField(widget=forms.Textarea)
    perfil = forms.CharField(widget=forms.Textarea)
    cant_vacantes = forms.IntegerField()
    observaciones = forms.CharField(widget=forms.Textarea)
    lugar_trabajo = forms.CharField(max_length=100)
    conocimientos = forms.CharField(widget=forms.Textarea)
    experiencia = forms.FloatField()
    #tipo_contrato = forms.CharField(max_length=20)
    #tipo_contrato = forms.CharField(max_length=20, choices= Oferta.TipoContrato.choices, default= Oferta.TipoContrato.INDEFINIDO)
    tipo_contrato = forms.ChoiceField( choices= Oferta.TipoContrato.choices)
    contacto = forms.CharField(max_length=50)
    remuneracion = forms.FloatField()
    informacion = forms.CharField(widget=forms.Textarea)
    funciones = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Oferta
        fields = '__all__'
