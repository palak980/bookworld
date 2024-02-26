# from rest_framework.response import Response
# from rest_framework import status
# from .models import *
# from .serializers import *
# from rest_framework import viewsets
# from rest_framework.decorators import api_view

# # Create your views here.


# @api_view(["GET"])
# def sem_product(request):
#     if request.method == "GET":
#         data = Catagory.objects.all()
#         serializer = SemProductSerializer(data,many = True)
#         return Response({"data":serializer.data})
        





# class Catagorys(viewsets.ModelViewSet):

#     queryset = Catagory.objects.all()
#     serializer_class = CatagorySerializer
    

# class Products(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
from .models import Catagory ,Product
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CatagorySerializer , ProductSerializer


class CatagoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows candidate to be viewed or edited.
    """
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer
    permission_classes = [permissions.AllowAny]


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows candidate to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


    
