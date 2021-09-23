from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# from rest_framework.authtoken.admin import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Userss, Product, Order
from . serializers import userSerializers, productSerializers, orderSerializers


# Create your views here.
class userList(APIView):

    def get(self, request):
        user1 = Userss.objects.all();
        serializer = userSerializers(user1, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.method = 'POST'
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        # user = User.objects.create_user(firstname=firstname, lastname=lastname )
        user.save()

class productsList(APIView):

    def get(self, request):
        product1 = Product.objects.all();
        serializer = productSerializers(product1, many=True)
        return Response(serializer.data)
    def post(self,request):
        pass

class ordersList(APIView):

    def get(self, request):
        order1 = Order.objects.all();
        serializer = orderSerializers(order1, many=True)
        return Response(serializer.data)
    def post(self):
        pass
