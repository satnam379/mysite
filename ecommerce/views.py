from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
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

    # def post(self, request):
    #     request.method = 'POST'
    #     firstname = request.POST.get('firstname')
    #     lastname = request.POST.get('lastname')
    #     # user = User.objects.create_user(firstname=firstname, lastname=lastname )
    #     user.save()
    def post(self, request, *args, **kwargs):
        all_data = request.data
        print(all_data)
        user = Userss.objects.create(firstname=all_data["firstname"], lastname=all_data["lastname"], mobile_number=all_data["mobile_number"], email=all_data["email"], password=all_data["password"])

        user.save()
        serializer = userSerializers(user)
        return Response(serializer.data, status=None)

    def put(self, request, *args, **kwargs):
        id = request.data("pk")
        # id = request.query_params["pk"]
        user = Userss.objects.get(id=id)

        data = request.data

        user.firstname = data["firstname"]
        user.lastname = data["lastname"]
        user.email = data["email"]
        user.mobile_number = data["mobile_number"]
        user.password = data["password"]

        user.save()

        serializer = userSerializers(user)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        id = kwargs["pk"]
        try:
            query = Userss.objects.get(pk=id)
            query.delete()
            return HttpResponse("Deleted!")
        except:
            return HttpResponseNotFound()

class productsList(APIView):

    def get(self, request):
        product1 = Product.objects.all();
        serializer = productSerializers(product1, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        all_data = request.data
        print(all_data)
        product = Product.objects.create(productname=all_data["productname"], price=all_data["price"],
                                     description=all_data["description"],)

        product.save()
        serializer = productSerializers(product)
        return Response(serializer.data, status=None)

    def put(self,  request, pk,):
        # id = request.query_params["id"]
        prduct = Userss.objects.get(pk)

        data = request.data

        prduct.productname = data["productname"]
        prduct.price = data["price"]
        prduct.description = data["description"]

        prduct.save()

        serializer = userSerializers(prduct)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        id = kwargs["pk"]
        try:
            query = Product.objects.get(pk=id)
            query.delete()
            return HttpResponse("Deleted!")
        except:
            return HttpResponseNotFound()

class ordersList(APIView):

    def get(self, request):
        order1 = Order.objects.all();
        serializer = orderSerializers(order1, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        all_data = request.data
        print(all_data)
        order = Order.objects.create(products=all_data["products"], user=all_data["user"],
                                     amount=all_data["amount"])

        order.save()
        serializer = userSerializers(order)
        return Response(serializer.data, status=None)

    def put(self, request, *args, **kwargs):
        id = request.query_params["id"]
        order = Userss.objects.get(id=id)

        data = request.data

        order.products = data["products"]
        order.user = data["user"]
        order.amount = data["amount"]

        order.save()

        serializer = userSerializers(order)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        id = kwargs["pk"]
        try:
            query = Order.objects.get(pk=id)
            query.delete()
            return HttpResponse("Deleted!")
        except:
            return HttpResponseNotFound()
