from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import SystemUsers
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, UserAdmin
from django.utils.translation import gettext, gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = SystemUsers
    list_display = ['email', 'username','first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal Information'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Audit'), {'fields': ('last_login', 'date_joined')}),
    )


#admin.site.unregister(SystemUsers)
admin.site.register(SystemUsers, CustomUserAdmin)
