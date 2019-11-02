from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    readonly_fields = [
        'date_joined',
        # 'staff_status'
        'last_login',
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['username'].disabled = True
               
        return form

    