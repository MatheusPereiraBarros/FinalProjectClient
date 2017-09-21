"""gerenbus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from empresa import views
from django.conf.urls.static import static
from .views import *
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken import views as rest_framework_views

schema_view = get_swagger_view(title='GerenBus')


urlpatterns = [
  url(r'^$', APIRoot.as_view(), name='root'),
  url(r'^users/$', UserList.as_view(), name=UserList.name),
  url(r'^viagens/$', viagens_list.as_view(), name=viagens_list.name),
  url(r'^viagem/(?P<pk>[0-9]+)/$', viagens_detail.as_view(), name=viagens_detail.name),
  url(r'^funcionarios/$', funcionarios_list.as_view(), name=funcionarios_list.name),
  url(r'^funcionario/(?P<pk>[0-9]+)/$', funcionarios_detail.as_view(), name=funcionarios_detail.name),
  url(r'^funcoes/$', funcoes_list.as_view(), name=funcoes_list.name),
  url(r'^funcao/(?P<pk>[0-9]+)/$', funcoes_detail.as_view(), name=funcoes_detail.name),
  url(r'^rotas/$', rotas_list.as_view(), name=rotas_list.name),
  url(r'^rota/(?P<pk>[0-9]+)/$', rotas_detail.as_view(), name=rotas_detail.name),
  url(r'^onibus_list/$', onibus_list.as_view(), name=onibus_list.name),
  url(r'^onibus_detail/(?P<pk>[0-9]+)/$', onibus_detail.as_view(), name=onibus_detail.name),
  url(r'^garagens/$', garagens_list.as_view(), name=garagens_list.name),
  url(r'^garagem/(?P<pk>[0-9]+)/$', garagens_detail.as_view(), name=garagens_detail.name),
  url(r'^swagger/$', schema_view, name='swagger'),
  url(r'^token/$', rest_framework_views.obtain_auth_token, name='api-token')
]

