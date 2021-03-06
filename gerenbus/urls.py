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

from django.contrib import admin
from django.conf.urls import url, include
#from rest_framework.authtoken import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('empresa.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
 #   url(r'^api-token-auth/', authviews.obtain_auth_token),
 #   url(r'^login/$', views.get_auth_token, name='login'),
 #   url(r'^logout/$', views.logout_user, name='logout'),
 #   url(r'^auth/$', views.login_form, name='login_form'),
]
    #url(r'^apiauth/', include('rest_framework.urls', namespace='rest_framework'))


