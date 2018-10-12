from django.db import models
from django.utils import timezone
class Post(models.Model):
        author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
        title = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title

class persona(models.Model):
        autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
        apellido = models.CharField(max_length=200)
        nombre = models.CharField(max_length=200)
        DNI = models.CharField(max_length=200)
        edad = models.CharField(max_length=200)
        fecha_nac = models.DateTimeField(
                blank=True, null=True)
        fechaalta = models.DateTimeField(
                default=timezone.now)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title

