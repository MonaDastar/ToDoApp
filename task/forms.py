from django import forms
from task.models import User

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'address']
