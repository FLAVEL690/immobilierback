from rest_framework import serializers

from .models import *

class houseSerializer(serializers.ModelSerializer):

    class Meta:
        model = House
        fields = ('category', 'image','price','description','ville', 'quartier', 'Nom_proprio', 'tel_proprio', 'date_added')
        

class meublesSerializer(serializers.ModelSerializer):

    class Meta:
        model = meubles
        fields = ('image', 'price','description','ville','quartier', 'Nom_entreprise', 'tel_entreprise', 'date_added')

        