from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeeSerializers


# Create your views here.
class employeeList(APIView):

    def get_queryset(self):
        emp = employees.objects.all();
        return emp
    def get(self, request, *args, **kwargs):
        # employees1 = employees.objects.all();
        employees1 = self.get_queryset()
        serializer = employeeSerializers(employees1, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        all_data = request.data
        print(all_data)
        new_emp = employees.objects.create(firstname=all_data["firstname"], lastname=all_data["lastname"])
        # request.method = 'POST'
        # firstname = request.POST.get('firstname')
        # lastname = request.POST.get('lastname')
        # # user = User.objects.create_user(firstname=firstname, lastname=lastname )
        new_emp.save()
        serializer = employeeSerializers(new_emp)
        return Response(serializer.data, status=None)


    # def post(self, request):
    #     if request.is_ajax():
    #         data = {"firstname": "harsh", "lastname": "kumar"}
    #         print
    #         request.POST.get('value')
    #         return RsonResponse(data)