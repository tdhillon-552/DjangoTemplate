from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import SystemUsers


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = SystemUsers
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = SystemUsers
        fields = ('username', 'email')
