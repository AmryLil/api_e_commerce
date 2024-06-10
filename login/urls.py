from django.urls import path
from . import views
from .viewset import LoginView, SignupView

urlpatterns = [
  path('login/',views.login,name='register'),
  path('singup/',views.singup,name='singup'),
  path('api/login/', LoginView.as_view(), name='login'),
  path('api/signup/', SignupView.as_view(), name='signup'),
  # path('login/',views.loginhandle,name='login'),
]