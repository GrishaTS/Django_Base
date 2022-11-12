from django.contrib import admin

from .models import Category, GalleryImage, Item, Preview, Tag

admin.site.register(Category)
admin.site.register(Tag)


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    readonly_fields = 'image_tmb',


class PreviewInline(admin.TabularInline):
    model = Preview
    readonly_fields = 'image_tmb',


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = 'name', 'category', 'is_published', 'image_tmb_small',
    list_editable = 'is_published',
    list_display_links = 'name',
    filter_horizontal = 'tags',
    inlines = [
        PreviewInline,
        GalleryImageInline,
    ]

    def image_tmb_small(self, obj):
        if obj.photo:
            return obj.photo.image_tmb_small()
        return "Нет изображения"
