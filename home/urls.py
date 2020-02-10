from django.urls import path
from . import views

urlpatterns = [
    path('', views.semigroup_view, name='home'),
]
