from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
# Create your views here.


class HelloOrderView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "hi akin"}, status= HTTP_200_OK)