from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Usuario

class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # claims extras embutidos no payload do token
        token['tipo'] = user.tipo
        token['username'] = user.username
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        # campos extras na RESPOSTA do login (fora do token)
        data['tipo'] = self.user.tipo
        return data


class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password',
        'tipo', 'data_nasc', 'cidade',]

    def create(self, validated_data):
    # create_user faz o hash da senha corretamente
        senha = validated_data.pop('password')
        usuario = Usuario(**validated_data)
        usuario.set_password(senha)
        usuario.save()
        return usuario