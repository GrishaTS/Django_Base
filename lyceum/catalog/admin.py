from django.contrib import admin

from .models import Category, Gallery, Item, OneImage, Tag

admin.site.register(Category)
admin.site.register(Tag)


@admin.register(OneImage)
class OneImageAdmin(admin.ModelAdmin):
    list_display = 'name', 'image_tmb'


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = 'name', 'image_tmb'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = 'name', 'is_published', 'preview'
    list_editable = 'is_published',
    list_display_links = 'name',
    filter_horizontal = 'tags',
