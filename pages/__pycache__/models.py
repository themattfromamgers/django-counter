from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name="film adı")
    desc = models.TextField(verbose_name="açuıklama")
    image = models.CharField(max_length=50, verbose_name="resim")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="tarih")
    isPublished = models.BooleanField(default= True,)
    
def __str__(self):
    return self.name