from django.db import models

# Create your models here.
class electronicsProjects(models.Model):
    CATAGORY = [
        ('RASPBERRY PI', 'raspberry pi'),
        ('CIRCUIT', 'circuit'),
        ('ROBOTICS', 'robotics'),
        ('GADGETS', 'gadgets')
    ]
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    catagory = models.CharField(max_length=50, choices=CATAGORY, null=True, blank=True, unique=False)
    video = models.FileField(upload_to = 'static/video/%y', null=True, blank=True)
    image = models.ImageField(upload_to = 'static/images', null=True, blank=True)
    description = models.CharField(max_length=500, null=True, unique=False, blank=False)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Electroniocs Projects"

    def __str__(self):
        return self.name
