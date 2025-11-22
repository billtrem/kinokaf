from django.contrib import admin
from django.utils.html import format_html
from .models import LandingAsset


@admin.register(LandingAsset)
class LandingAssetAdmin(admin.ModelAdmin):
    list_display = ("title", "thumbnail", "created_at")
    readonly_fields = ("preview",)

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="80" style="border-radius:5px;" />',
                obj.image.url
            )
        return "(No image)"
    thumbnail.short_description = "Image"

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="300" style="border-radius:10px;" />',
                obj.image.url
            )
        return "No image uploaded"


