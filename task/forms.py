from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['titulo', 'descripción', 'importante']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe un titulo'}),
            'descripción': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe una descripción'}),
            'importante': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }