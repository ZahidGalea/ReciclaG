from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from bootstrap_datepicker_plus import TimePickerInput
from django.contrib.auth.forms import AuthenticationForm

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from . import models

ENABLED_HOURS = [value for value in range(0, 24)]


class UserCreationFormM(UserCreationForm):
    first_name = forms.CharField(label='Primer Nombre')
    last_name = forms.CharField(label='Apellido')
    email = forms.EmailField(label='Correo Electrónico')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'register'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'get'
        self.helper.form_action = 'dashboard'
        self.helper.add_input(Submit('submit', 'Registrate'))

        self.fields['username'].label = "Nombre de Usuario"
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirma Contraseña"

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class InscribirPunto(forms.ModelForm):
    titulo = forms.CharField(label='Titulo del punto', max_length=50)
    region = forms.CharField(label='Región', max_length=50)
    comuna = forms.CharField(label='Comuna', max_length=50)
    direccion = forms.CharField(label='Dirección', max_length=100)

    material_lata = forms.BooleanField(label='Lata', required=False)
    material_papel = forms.BooleanField(label='Papel', required=False)
    material_carton = forms.BooleanField(label='Carton', required=False)
    material_plastico = forms.BooleanField(label='Plastico', required=False)
    material_vidrio = forms.BooleanField(label='Vidrio', required=False)

    ruta_imagen = forms.ImageField(label='Imagen', required=False)
    horario_oficina = forms.BooleanField(label='Horario oficina', required=False)

    horario_apert_lunes = forms.TimeField(label='Apertura Lunes', required=False,
                                          widget=TimePickerInput(format='%H:%S').start_of('lunes'))
    horario_cierr_lunes = forms.TimeField(label='Cierre Lunes', required=False,
                                          widget=TimePickerInput(format='%H:%S').end_of('lunes'))
    horario_apert_martes = forms.TimeField(label='Apertura Martes', required=False,
                                           widget=TimePickerInput(format='%H:%S').start_of('martes'))
    horario_cierr_martes = forms.TimeField(label='Cierre Martes', required=False,
                                           widget=TimePickerInput(format='%H:%S').end_of('martes'))
    horario_apert_miercoles = forms.TimeField(label='Apertura Miercoles', required=False,
                                              widget=TimePickerInput(format='%H:%S').start_of('miercoles'))
    horario_cierr_miercoles = forms.TimeField(label='Cierre Miercoles', required=False,
                                              widget=TimePickerInput(format='%H:%S').end_of('miercoles'))
    horario_apert_jueves = forms.TimeField(label='Apertura Jueves', required=False,
                                           widget=TimePickerInput(format='%H:%S').start_of('jueves'))
    horario_cierr_jueves = forms.TimeField(label='Cierre Jueves', required=False,
                                           widget=TimePickerInput(format='%H:%S').end_of('jueves'))
    horario_apert_viernes = forms.TimeField(label='Apertura Viernes', required=False,
                                            widget=TimePickerInput(format='%H:%S').start_of('viernes'))
    horario_cierr_viernes = forms.TimeField(label='Cierre Viernes', required=False,
                                            widget=TimePickerInput(format='%H:%S').end_of('viernes'))
    horario_apert_sabado = forms.TimeField(label='Apertura Sabado', required=False,
                                           widget=TimePickerInput(format='%H:%S').start_of('sabado'))
    horario_cierr_sabado = forms.TimeField(label='Cierre Sabado', required=False,
                                           widget=TimePickerInput(format='%H:%S').end_of('sabado'))
    horario_apert_domingo = forms.TimeField(label='Apertura Domingo', required=False,
                                            widget=TimePickerInput(format='%H:%S').start_of('domingo'))
    horario_cierr_domingo = forms.TimeField(label='Cierre Domingo', required=False,
                                            widget=TimePickerInput(format='%H:%S').end_of('domingo'))

    def __init__(self, *args, **kwargs):
        super(InscribirPunto, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'inscribirPunto'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'dashboard'
        self.helper.add_input(Submit('submit', 'Inscribir'))

    class Meta:
        model = models.PuntoReciclag
        fields = ['titulo', 'region', 'comuna', 'direccion', 'material_lata', 'material_papel', 'material_carton',
                  'material_vidrio', 'material_plastico', 'ruta_imagen',
                  'horario_oficina',
                  'horario_apert_lunes',
                  'horario_cierr_lunes',
                  'horario_apert_martes',
                  'horario_cierr_martes',
                  'horario_apert_miercoles',
                  'horario_cierr_miercoles',
                  'horario_apert_jueves',
                  'horario_cierr_jueves',
                  'horario_apert_viernes',
                  'horario_cierr_viernes',
                  'horario_apert_sabado',
                  'horario_cierr_sabado',
                  'horario_apert_domingo',
                  'horario_cierr_domingo']

        field_order = ['titulo', 'region', 'comuna', 'direccion',
                       'material_lata',
                       'material_papel',
                       'material_carton',
                       'material_vidrio',
                       'material_plastico'
                       'ruta_imagen',
                       'horario_oficina',
                       'horario_apert_lunes',
                       'horario_cierr_lunes',
                       'horario_apert_martes',
                       'horario_cierr_martes',
                       'horario_apert_miercoles',
                       'horario_cierr_miercoles',
                       'horario_apert_jueves',
                       'horario_cierr_jueves',
                       'horario_apert_viernes',
                       'horario_cierr_viernes',
                       'horario_apert_sabado',
                       'horario_cierr_sabado',
                       'horario_apert_domingo',
                       'horario_cierr_domingo']


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'login'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'get'
        self.helper.form_action = 'dashboard'
        self.helper.add_input(Submit('submit', 'Loguearse'))

        self.fields['username'].label = "Nombre de Usuario"
        self.fields['password'].label = "Contraseña"

    class Meta:
        model = models.User
        fields = ('username', 'password')


class ModificarPunto(forms.ModelForm):
    titulo = forms.CharField(label='Titulo del punto', max_length=50)
    region = forms.CharField(label='Región', max_length=50)
    comuna = forms.CharField(label='Comuna', max_length=50)
    direccion = forms.CharField(label='Dirección', max_length=100)

    material_lata = forms.BooleanField(label='Lata', required=False)
    material_papel = forms.BooleanField(label='Papel', required=False)
    material_carton = forms.BooleanField(label='Carton', required=False)
    material_plastico = forms.BooleanField(label='Plastico', required=False)
    material_vidrio = forms.BooleanField(label='Vidrio', required=False)

    ruta_imagen = forms.ImageField(label='Imagen', required=False)
    horario_oficina = forms.BooleanField(label='Horario oficina', required=False)

    horario_apert_lunes = forms.TimeField(label='Apertura Lunes', required=False,
                                          widget=TimePickerInput(format='%H:%S').start_of('lunes'))
    horario_cierr_lunes = forms.TimeField(label='Cierre Lunes', required=False,
                                          widget=TimePickerInput(format='%H:%S').end_of('lunes'))
    horario_apert_martes = forms.TimeField(label='Apertura Martes', required=False,
                                           widget=TimePickerInput(format='%H:%S').start_of('martes'))
    horario_cierr_martes = forms.TimeField(label='Cierre Martes', required=False,
                                           widget=TimePickerInput(format='%H:%S').end_of('martes'))
    horario_apert_miercoles = forms.TimeField(label='Apertura Miercoles', required=False,
                                              widget=TimePickerInput(format='%H:%S').start_of('miercoles'))
    horario_cierr_miercoles = forms.TimeField(label='Cierre Miercoles', required=False,
                                              widget=TimePickerInput(format='%H:%S').end_of('miercoles'))
    horario_apert_jueves = forms.TimeField(label='Apertura Jueves', required=False,
                                           widget=TimePickerInput(format='%H:%S').start_of('jueves'))
    horario_cierr_jueves = forms.TimeField(label='Cierre Jueves', required=False,
                                           widget=TimePickerInput(format='%H:%S').end_of('jueves'))
    horario_apert_viernes = forms.TimeField(label='Apertura Viernes', required=False,
                                            widget=TimePickerInput(format='%H:%S').start_of('viernes'))
    horario_cierr_viernes = forms.TimeField(label='Cierre Viernes', required=False,
                                            widget=TimePickerInput(format='%H:%S').end_of('viernes'))
    horario_apert_sabado = forms.TimeField(label='Apertura Sabado', required=False,
                                           widget=TimePickerInput(format='%H:%S').start_of('sabado'))
    horario_cierr_sabado = forms.TimeField(label='Cierre Sabado', required=False,
                                           widget=TimePickerInput(format='%H:%S').end_of('sabado'))
    horario_apert_domingo = forms.TimeField(label='Apertura Domingo', required=False,
                                            widget=TimePickerInput(format='%H:%S').start_of('domingo'))
    horario_cierr_domingo = forms.TimeField(label='Cierre Domingo', required=False,
                                            widget=TimePickerInput(format='%H:%S').end_of('domingo'))

    def __init__(self, *args, **kwargs):
        super(ModificarPunto, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'modificarPunto'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'dashboard'
        self.helper.add_input(Submit('submit', 'Modificar'))

    class Meta:
        model = models.PuntoReciclag
        fields = ['titulo', 'region', 'comuna', 'direccion', 'material_lata', 'material_papel', 'material_carton',
                  'material_vidrio', 'material_plastico', 'ruta_imagen',
                  'horario_oficina',
                  'horario_apert_lunes',
                  'horario_cierr_lunes',
                  'horario_apert_martes',
                  'horario_cierr_martes',
                  'horario_apert_miercoles',
                  'horario_cierr_miercoles',
                  'horario_apert_jueves',
                  'horario_cierr_jueves',
                  'horario_apert_viernes',
                  'horario_cierr_viernes',
                  'horario_apert_sabado',
                  'horario_cierr_sabado',
                  'horario_apert_domingo',
                  'horario_cierr_domingo']

        field_order = fields
