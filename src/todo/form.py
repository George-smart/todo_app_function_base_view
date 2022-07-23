# from django.contrib.auth import forms
from .models import TodoApp
from django import forms



class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoApp
        fields = ['todo']
        
        
        widgets = {
            'todo': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'exampleFormControlInput1', 'placeholder': 'Add a Todo'})
        }