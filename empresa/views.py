#from django.contrib.auth.models import User, Group
from django.urls import reverse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.utils import timezone
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class viagens_detail(generics.RetrieveUpdateDestroyAPIView):

  queryset = Viagem.objects.all()
  serializer_class = ViagemSerializer
  name = 'viagem-detail'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class onibus_detail(generics.RetrieveUpdateDestroyAPIView):

  queryset = Onibus.objects.all()
  serializer_class = OnibusSerializer
  name = 'onibus-detail'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class garagens_detail(generics.RetrieveUpdateDestroyAPIView):
  
  queryset = Garagem.objects.all()
  serializer_class = GaragemSerializer
  name = 'garagem-detail'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class funcoes_detail(generics.RetrieveUpdateDestroyAPIView):
 
  queryset = Funcao.objects.all()
  serializer_class = FuncaoSerializer
  name = 'funcao-list'
  permission_classes = (permissions.IsAuthenticated,)

class rotas_detail(generics.RetrieveUpdateDestroyAPIView):
  
  queryset = Rota.objects.all()
  serializer_class = RotaSerializer
  name = 'rota-detail'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class funcionarios_detail(generics.RetrieveUpdateDestroyAPIView):

  queryset = Funcionario.objects.all()
  serializer_class = FuncionarioSerializer
  name = 'funcionario-detail'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class funcoes_list(generics.ListCreateAPIView):
 
  queryset = Funcao.objects.all()
  serializer_class = FuncaoSerializer
  name = 'funcao-list'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class funcionarios_list(generics.ListCreateAPIView):
  
  queryset = Funcionario.objects.all()
  serializer_class = FuncionarioSerializer
  name = 'funcionario-list'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
  filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
  ordering_fields = ('nome',)
  search_fields = ('nome',)
  filter_fields = ('nome',)


class rotas_list(generics.ListCreateAPIView):

  queryset = Rota.objects.all()
  serializer_class = RotaSerializer
  name = 'rota-list'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
  filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
  ordering_fields = ('nomeRota',)
  search_fields = ('nomeRota',)
  filter_fields = ('nomeRota',)

class onibus_list(generics.ListCreateAPIView):

  queryset = Onibus.objects.all()
  serializer_class = OnibusSerializer
  name = 'onibus-list'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class garagens_list(generics.ListCreateAPIView):

  queryset = Garagem.objects.all()
  serializer_class = GaragemSerializer
  name = 'garagem-list'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
  
  
'''
class viagens_list(generics.ListCreateAPIView):

  queryset = Viagem.objects.all()
  serializer_class = ViagemSerializer
  name = 'viagens-list'
  http_method_names = ['get', 'delete', 'head', 'options']
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
  
  def create(self, request):
    serializer = ViagemSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      if request.user != serializer.validated_data.get('idFuncionario').funcionario.user:
        content = {
          "detail": "Não autorizado"
        }
        return Response(content, status=status.HTTP_403_FORBIDDEN)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
class viagens_list(generics.ListCreateAPIView):

  queryset = Viagem.objects.all()
  serializer_class = ViagemSerializer
  name = 'viagens-list'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserList(generics.ListAPIView):

  queryset = User.objects.all()
  serializer_class = UserSerializer
  name = 'user-list'
  permission_classes = (permissions.IsAuthenticated,)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class APIRoot(generics.GenericAPIView):

  def get(self, request):
    return Response({'viagens': reverse(viagens_list.name, request=request),
                     'funcionarios': reverse(funcionarios_list.name, request=request),
                     'funcoes': reverse(funcoes_list.name, request=request),
                     'rotas': reverse(rotas_list.name, request=request),
                     'onibus': reverse(onibus_list.name, request=request),
                     'garagens': reverse(garagens_list.name, request=request),
                     'swagger': reverse('swagger', request=request)
                     })


