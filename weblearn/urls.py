from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views
from django.conf import settings
from rest_framework import routers
from login.viewset import LoginView, SignupView

router = routers.DefaultRouter()



urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('',include('login.urls')),
    path('',include('seller.urls')),
    path('',include('myaccount.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
