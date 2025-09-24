from django.contrib import admin
from .models import Language, Topic, Content


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'language')
    list_filter = ('language',)
    search_fields = ('title', 'language__name')


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('topic', 'link')
    list_filter = ('topic',)
    search_fields = ('text', 'code', 'topic__title')
