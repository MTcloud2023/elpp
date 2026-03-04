from django.db import models

# Create your models here.

from django.db import models

class UserSurvey(models.Model):
    nombre = models.CharField(max_length=100)

    opcion_principal = models.CharField(max_length=50)

    pregunta1 = models.TextField()
    pregunta2 = models.CharField(max_length=10)
    pregunta2_detalle = models.TextField(blank=True, null=True)

    pregunta3 = models.IntegerField()

    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    pregunta5 = models.TextField()

    pregunta6 = models.CharField(max_length=50)
    pregunta7 = models.CharField(max_length=20, null=True, blank=True)
    pregunta8 = models.CharField(max_length=20, null=True, blank=True)
    pregunta9 = models.CharField(max_length=20, null=True, blank=True)
    pregunta10 = models.CharField(max_length=20, null=True, blank=True)
    pregunta11 = models.CharField(max_length=20, null=True, blank=True)
    pregunta12 = models.CharField(max_length=20, null=True, blank=True)

    imagen = models.ImageField(upload_to="user_survey_images/")

    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

