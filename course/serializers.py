from rest_framework import serializers
from .models import Language, Topic, Content




class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('name', 'slug','image')


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('language', 'title','order')


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('topic', 'text','link', 'code', 'video_url', 'order')


