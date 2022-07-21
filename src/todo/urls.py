from django.urls import path
from .views import index, signup, signin

urlpatterns = [
    path('', index, name='home'),
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
]
