from django.db import models
from django import forms


# Create your models here.

CATEGORY =(
("M", "Maison"),
("A", "Studio"),
("S", "Studio"),
("C", "Chambre"),
)
class House(models.Model):
    category = forms.ChoiceField(choices=CATEGORY)
    image = models.CharField(max_length=500)
    price = models.FloatField()
    description = models.TextField()
    ville = models.CharField(max_length=50)
    quartier = models.CharField(max_length=200)
    Nom_propio = models.CharField(max_length=50)
    tel_proprio = models.IntegerField
    date_added =models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']


class meubles(models.Model):
    
    image = models.CharField(max_length=500)
    price = models.FloatField()
    description = models.TextField()
    ville = models.CharField(max_length=50)
    quartier = models.CharField(max_length=200)
    Nom_entreprise = models.CharField(max_length=50)
    tel_entreprise = models.IntegerField
    date_added =models.DateTimeField(auto_now=True)

class Meta:
    ordering = ['-date_added']
