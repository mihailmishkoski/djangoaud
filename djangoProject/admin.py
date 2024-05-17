from django.contrib import admin
from .models import Musician, Album


class PersonAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]


class AlbumInlineAdmin(admin.TabularInline):
    model = Album
    extra = 1


class MusicianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'instrument')
    search_fields = ('first_name', 'last_name', 'instrument')
    inlines = [AlbumInlineAdmin]


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'release_date', 'num_stars')
    list_filter = ('release_date', 'num_stars')
    search_fields = ('name', 'artist__first_name', 'artist__last_name')
    date_hierarchy = 'release_date'


admin.site.register(Musician, MusicianAdmin)
admin.site.register(Album, AlbumAdmin)
