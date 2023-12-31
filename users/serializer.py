from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'username', 'password','address', 'avatar')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        address = validated_data.pop('address', None)
        # avatar = validated_data.pop('avatar', None)
        user = UserProfile.objects.create_user(**validated_data, address=address)
        return user
