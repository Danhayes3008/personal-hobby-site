from tabnanny import verbose
from django.db import models
from django.forms import DateField

# Create your models here.
class blenderModels(models.Model):
    CATAGORY = [
        ('PLANET', 'planet'),
        ('SHIP', 'ship'),
        ('BUILDING', 'building'),
        ('OBJECT', 'object')
    ]
    name = models.CharField(max_length=50, null=True, unique=True, blank=False)
    catagory = models.CharField(max_length=50, choices=CATAGORY, null=True, blank=True, unique=False)
    video = models.FileField(upload_to = 'static/video/%y', null=True, blank=True)
    image = models.ImageField(upload_to = 'media/static/images', null=True, blank=True)
    description = models.CharField(max_length=500, null=True, unique=False, blank=False)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Blender Models"

    def __str__(self):
        return self.name
