from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, House


# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone' , 'username' ,'is_resident', 'is_security')
    list_editable = ['is_resident', 'is_security']
    list_display_links = ['first_name', 'last_name']
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2" , "first_name", "last_name", "phone", "email"),
            },
        ),
    )

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('house_number', 'address', 'user')


