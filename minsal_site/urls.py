from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('blog/',formulario,name='formulario'),
]