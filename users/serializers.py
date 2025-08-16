from rest_framework import serializers
from .models import CustomUser, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('nome_completo', 'telefone', 'tipo_usuario')

class UserRegistrationSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = CustomUser.objects.create_user(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user