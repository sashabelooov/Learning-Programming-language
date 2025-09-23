from django.contrib import admin
from .models import Language, Topic, Content



# Language admin
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}  # slug avtomatik hosil qilinadi
    search_fields = ('name',)  # Language nomi bo‘yicha qidiruv



# Topic admin
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'order')
    list_filter = ('language',)
    ordering = ('language', 'order')
    search_fields = ('title', 'language__name')  # Topic nomi va tegishli language nomi bo‘yicha qidiruv



# Content admin
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('topic', 'order', 'text', 'link', 'video_url')
    list_filter = ('topic',)
    ordering = ('topic', 'order')
    search_fields = ('text', 'code', 'topic__title')  # Content matni, code snippet va topic nomi bo‘yicha qidiruv
