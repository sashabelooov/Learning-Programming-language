from django.contrib import admin
from .models import Language, Topic, Content, Comment, Rating


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'language', 'slug', 'order']
    prepopulated_fields = {'slug': ('title',)}  # Slugni avtomatik to'ldirish


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('topic', 'link')
    list_filter = ('topic',)
    search_fields = ('text', 'code', 'topic__title')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'short_text', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('text', 'user__username', 'content__text')

    def short_text(self, obj):
        # Juda uzun textlarni qisqa ko‘rsatish uchun
        return (obj.text[:75] + '...') if len(obj.text) > 75 else obj.text
    short_text.short_description = 'Comment Text'

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'rating', 'created_at')
    list_filter = ('rating', 'created_at', 'user')
    search_fields = ('user__username', 'content__text')