from rest_framework import serializers
from .models import Songs, Token

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        #field = ()
        fields = '__all__'

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'
