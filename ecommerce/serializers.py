from rest_framework import serializers
from . models import Userss, Product, Order

class userSerializers(serializers.ModelSerializer):

    class Meta:
        model = Userss
        fields = ('pk', 'firstname', 'lastname', 'email', 'mobile_number')
        fields = '__all__'

class productSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        # fields = ('firstname', 'lastname')
        fields = '__all__'

class orderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        # fields = ('firstname', 'lastname')
        fields = '__all__'
