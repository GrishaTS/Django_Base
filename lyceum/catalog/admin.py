from django.contrib import admin

from .models import Category, Item, Tag, OneImage, Gallery

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(OneImage)
admin.site.register(Gallery)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = 'name', 'is_published', 'image_tmb'
    list_editable = 'is_published',
    list_display_links = 'name',
    filter_horizontal = 'tags',
