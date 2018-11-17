"""EmailSending URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from HomePage.views import home_page
from Registration.views import create_regis
from Sending.views import SendPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('registration/', create_regis, name='register'),
    path('sending/', SendPage, name='sending')
]
