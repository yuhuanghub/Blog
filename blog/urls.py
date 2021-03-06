"""blog URL Configuration

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
from app01 import views
from django.conf.urls import include
# from django.views import static
# from django.conf import settings
# from app01.uploads import upload_image

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index$', views.index),
    url(r'^login/$', views.login),
    url(r'^content_detail-(?P<uid>\d+)', views.content_detail),
    url(r'django$',views.django_url),
    url(r'ml$',views.ml),
    url(r'python$',views.python)
]
