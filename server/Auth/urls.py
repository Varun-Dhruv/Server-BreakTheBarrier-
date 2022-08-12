from django.urls import path
from .views import *
urlpatterns = [
    # path('api/',),
    path('Signup', Signup, name="Signup"),
    path('Login', Login, name="Login"),
]
