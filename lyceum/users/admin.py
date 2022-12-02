from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CreateProfileForm, UpdateProfileForm
from .models import Profile


@admin.register(Profile)
class CastomUserAdmin(UserAdmin):
    model = Profile
    form = UpdateProfileForm
    add_form = CreateProfileForm
    list_display = ('email', 'first_name', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('birthday',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'birthday',
                'password1',
                'password2',
                'is_staff',
                'is_active'
            ),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
