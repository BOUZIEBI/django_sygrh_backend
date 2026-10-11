from django.contrib import admin

from .models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "uid",
        "libelle",
        "code",
    )

    list_filter = ("is_mode",)
    search_fields = ("libelle", "code")