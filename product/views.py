from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions


# Create your views here.
class ProductView(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    permission_classes = [permissions.IsAdminUser]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SingleProductView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

 
