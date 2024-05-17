from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Data
from .serializers import DataSerializer

# Create your views here.

def testHello(request):
    return HttpResponse("Hello, World!") # Return a simple HTTP response

@api_view(['GET'])
def data_list(request):
    data = Data.objects.all()
    serializer = DataSerializer(data, many=True)
    return Response(serializer.data)