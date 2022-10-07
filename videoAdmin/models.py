from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    """ Usuarios  """
    numberId=models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    address=models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Peliculas(models.Model):
    """ Peliculas """   
    name = models.CharField(max_length=50)
    typeMovie= models.CharField(max_length=50)    
    pub_date = models.DateField(auto_now_add=True)    
    numberMovies = models.IntegerField()
    comment = models.CharField(max_length=200, blank=True)



