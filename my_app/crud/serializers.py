# convert instance of product object  into datatypes that reponse object can understand

from rest_framework import serializers
from crud.models import Product

class ProductSerializer(serializers.ModelSerializer): #inherits from serializer
    class Meta:
        model=Product
        fields='__all__'
