from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SingleProductView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

 
