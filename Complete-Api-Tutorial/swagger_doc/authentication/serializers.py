from rest_framework import serializers
from django.contrib.auth.models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=120)
    password = serializers.CharField(max_length=65, min_length=8)
    

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        # The field describe the things we allow the user to see in the response
        fields = ['username','first_name','last_name','email','password']

    # this method gets called before a user get created
    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email':('Email is already in use')})
        return super().validate(attrs)
    
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
        