from django.shortcuts import render

from home.models import Product
from rest_framework import generics

from home.serializers import ProductSerializer


# Create your views here.
class ProductApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
