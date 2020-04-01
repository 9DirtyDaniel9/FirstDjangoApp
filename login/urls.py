from django.urls import path
from . import views

urlpatterns = [
path('', views.MyprojectLoginView.as_view(), name='login'),
]
