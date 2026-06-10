from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer

from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer, UsuarioSerializer

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    # em urls.py, troque por:
    # path('login/', LoginView.as_view(), name='login'),

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = UsuarioSerializer(data=request.data)

    if serializer.is_valid():
        usuario = serializer.save()
        refresh = RefreshToken.for_user(usuario) # gera o par

        return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'usuario': serializer.data,
        }, 
        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated]) # JWT já é o default agora
def perfil(request):
    return Response({
        'username': request.user.username,
        'tipo': request.user.tipo,
        'mensagem': f'Autenticado via JWT como {request.user.get_tipo_display()}.'
        })
