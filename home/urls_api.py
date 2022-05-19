from django.urls import path
from .view_api import *

urlpatterns = [
  path('login/', LoginView),
  path('register/', RegisterView)

]
