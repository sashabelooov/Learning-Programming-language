from django.shortcuts import render, get_object_or_404
from django.shortcuts import get_object_or_404
from .models import Language, Topic, Content
from .serializers import LanguageSerializer, TopicSerializer, ContentSerializer



def language_view(request, language_slug):
    language = get_object_or_404(Language, slug=language_slug)
    # topics = language.topics.all().order_by("order")
    topics = language.topics.exclude(slug__isnull=True).exclude(slug="").order_by("order")

    print("Topics in view:", [(t.id, t.title, t.slug) for t in topics])

    return render(request, "topic.html", {
        "language": language,
        "topics": topics,
    })


def content_view(request, language_slug, topic_slug=None):
    language = get_object_or_404(Language, slug=language_slug)
    topics = language.topics.all().order_by("order")
    
    # Agar topic_slug berilgan bo'lsa, shu topicni olamiz
    topic = None
    contents = []
    if topic_slug:
        topic = get_object_or_404(Topic, language=language, slug=topic_slug)
        contents = topic.contents.all().order_by("order")
    
    return render(request, "content.html", {
        "language": language,
        "topics": topics,
        "current_topic": topic,
        "contents": contents,
    })