from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
    title=forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))
    class Meta:     # Meta means "metadata"
        model = Task
        fields = '__all__'