"""
URL configuration for propertyvaluation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from propval import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup',views.Signup,name='signup'),
    path('login/',views.Signin,name='login'),
    path('',views.Signin,name='login'),
    path('home/',views.Home,name='home'),
    path('deluser/<int:uid>/<int:udid>',views.del_user,name='deluser'),
    path('activateuser/<int:uid>',views.activateuser,name='activateuser'),
    path('logout/',views.Logout,name='logout'),
    path('api/', include("api.urls")),
    path('reception/', include("reception.urls")),
    path('engineer/', include("site_engineer.urls")),
    path('reporter/', include("reporter.urls")),
    path('propval/', include("propval.urls")),
    path('companyprofile/', views.company_profile_view, name='companyprofile'),
    path('banks/<int:uid>', views.banks, name='banks'),
    path('bankmanage', views.bankmanage, name='bankmanage'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOTPROFILE) 
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOTREPORTER)