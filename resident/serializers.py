from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from resident.models import House, User


class HouseSerializer(serializers.ModelSerializer):
    # Use PrimaryKeyRelatedField so DRF handles converting IDs to User instances
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = House
        fields = ['house_number', 'address', 'user']


# class AddUserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ['username', 'password','first_name']


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['username','first_name','last_name','email','password','phone']


class CreateInviteSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100 , allow_blank= False , allow_null=False)
    last_name = serializers.CharField(max_length=100, allow_blank= False , allow_null=False)
    phone_number = serializers.CharField(max_length=11, min_length= 11 , allow_blank= False)
    expires_at = serializers.DateTimeField()

