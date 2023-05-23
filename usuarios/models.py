from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class ExtraData(models.Model):
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    descripcion = RichTextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
