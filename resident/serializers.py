from rest_framework import serializers

from resident.models import House, User


class HouseSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField()
    class Meta:
        model = House
        fields = ['house_number', 'address', 'user']
      # Assuming resident is a username or email