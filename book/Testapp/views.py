from django.shortcuts import render

from rest_framework.generics import ListAPIView,ListCreateAPIView
from .models import Search
from .serializers import SearchSerializer
from rest_framework.filters import SearchFilter

# Create your views here.
class location(ListCreateAPIView):
    serializer_class = SearchSerializer
    queryset = Search.objects.all()



class Searchlist(ListAPIView):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    filter_backends = [SearchFilter]
    search_fields = ['location','services']
