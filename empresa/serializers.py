#from django.contrib.auth.models import User, Group

from rest_framework import serializers
#from empresa.models import Viagem
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
  	class Meta:
	    model = User
	    fields = ('username',)

class ViagemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Viagem
		fields = ('idViagem', 'horario', 'quantPassageiros', 'idRota', 'idOnibus', 'idFuncionario')
'''
class FuncionarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Funcionario
		fields = ('idFuncionario', 'nome', 'user', 'CPF', 'idFuncao')
'''
class FuncionarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Funcionario
		fields = ('idFuncionario', 'nome', 'CPF', 'idFuncao')

class FuncaoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Funcao
		fields = ('idFuncao', 'descricaoFuncao')

class RotaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rota
		fields = ('idRota', 'nomeRota', 'destino', 'partida', 'horario', 'diaDaSemana', 'valorPassagem')

class OnibusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Onibus
		fields = ('idOnibus', 'marcaOnibus', 'modeloOnibus', 'placa', 'garagem')

class GaragemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Garagem
		fields = ('idGaragem', 'endereco', 'quantVagas')


"""class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

"""

