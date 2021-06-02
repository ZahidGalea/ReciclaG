from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Usuario(models.Model):
    id_usuario = models.BigAutoField(primary_key=True, unique=True, auto_created=True,
                                     verbose_name='Id del usuario creado')
    organizacion = models.TextField(verbose_name='Nombre de la organización')
    telefono = PhoneNumberField()
    email = models.TextField(verbose_name='Correo electrónico de la persona')
    clave = models.TextField(verbose_name='Clave de login a la plataforma')

    def __str__(self):
        return self.id_usuario


class PuntoReciclag(models.Model):
    titulo = models.TextField(verbose_name='Titulo del punto')
    region = models.TextField(verbose_name='Región')
    comuna = models.TextField(verbose_name='Nombre de la comuna')
    direccion = models.TextField(verbose_name='Dirección')
    material_lata = models.BooleanField(default=False, verbose_name='Material lata')
    material_papel = models.BooleanField(default=False, verbose_name='Material papel')
    material_carton = models.BooleanField(default=False, verbose_name='Material cartón')
    material_plastico = models.BooleanField(default=False, verbose_name='Material plastico')
    material_vidrio = models.BooleanField(default=False, verbose_name='Material vidrio')
    ruta_imagen = models.ImageField(verbose_name='Ruta a la imagen del punto', upload_to='foto', null=True)
    horario_oficina = models.BooleanField(default=True, verbose_name='Opción de horario oficina')
    horario_apert_lunes = models.TimeField(null=True, verbose_name='Apertura Lunes')
    horario_cierr_lunes = models.TimeField(null=True, verbose_name='Cierre Lunes')
    horario_apert_martes = models.TimeField(null=True, verbose_name='Apertura Martes')
    horario_cierr_martes = models.TimeField(null=True, verbose_name='Cierre Martes')
    horario_apert_miercoles = models.TimeField(null=True, verbose_name='Apertura Miercoles')
    horario_cierr_miercoles = models.TimeField(null=True, verbose_name='Cierre Miercoles')
    horario_apert_jueves = models.TimeField(null=True, verbose_name='Apertura Jueves')
    horario_cierr_jueves = models.TimeField(null=True, verbose_name='Cierre Jueves')
    horario_apert_viernes = models.TimeField(null=True, verbose_name='Apertura Viernes')
    horario_cierr_viernes = models.TimeField(null=True, verbose_name='Cierre Viernes')
    horario_apert_sabado = models.TimeField(null=True, verbose_name='Apertura Sabado')
    horario_cierr_sabado = models.TimeField(null=True, verbose_name='Cierre Sabado')
    horario_apert_domingo = models.TimeField(null=True, verbose_name='Apertura Domingo')
    horario_cierr_domingo = models.TimeField(null=True, verbose_name='Cierre Domingo')

    # id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
