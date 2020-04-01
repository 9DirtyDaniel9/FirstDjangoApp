from django.conf.urls import url
from registration.views import signup

urlpatterns = [
    url('', signup, name='signup'),
]