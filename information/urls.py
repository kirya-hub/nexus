from django.urls import path
from .views import home

app_name = 'information'

urlpatterns = [
    path('', home, name='home'),
]
