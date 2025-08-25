from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    titulo= models.CharField(max_length=100)
    descripción = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    fechacompletado = models.DateTimeField(null=True, blank=True)
    importante = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + '- by ' + self.user.username