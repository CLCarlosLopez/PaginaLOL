from django.db import models
import datetime

class Campeones(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagenes = models.ImageField(upload_to="Campeones_img/images")
    date = models.DateField(datetime.date.today)