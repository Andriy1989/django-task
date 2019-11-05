from .models import User,Goods


from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'FirstName', 'LastName', 'BirthDate', 'RegistrationDate', 'Order_id']


class GoodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goods
        fields = ['id', 'GoodsName', 'GoodsPrice']