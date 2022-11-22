from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'text',
    )
    list_display_links = ('name',)
