from django.urls import path
from .views import index, signup, signin, signout, complete, editTodo, deleteTodo

urlpatterns = [
    path('', index, name='home'),
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('signout', signout, name='signout'),
    path('complete/<int:pk>', complete, name='complete'),
    path('update/<int:pk>', editTodo, name='update'),
    path('delete/<int:pk>', deleteTodo, name='delete'),
]
