from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """Admin interface for the custom user model."""
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'date_of_birth')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'date_of_birth')}),
    )

# Register the custom user model with the admin site
admin.site.register(CustomUser, CustomUserAdmin)
