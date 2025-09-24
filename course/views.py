from django.shortcuts import render, get_object_or_404
from django.shortcuts import get_object_or_404
from .models import Language, Topic, Content
from .serializers import LanguageSerializer, TopicSerializer, ContentSerializer



def language_view(request, language_slug):
    language = get_object_or_404(Language, slug=language_slug)
    topics = language.topics.all().order_by("order")

    return render(request, "topic.html", {
        "language": language,
        "topics": topics,
    })

def content_view(request, language_slug, topic_slug):
    # Tilni topamiz
    language = get_object_or_404(Language, slug=language_slug)

    # Barcha mavzular chap menyu uchun
    topics = language.topics.all().order_by("order")

    # Hozirgi topic
    current_topic = get_object_or_404(Topic, slug=topic_slug, language=language)

    # Shu topicga tegishli contentlar
    contents = current_topic.contents.all().order_by("order")

    return render(request, "content.html", {
        "language": language,
        "topics": topics,              # chap menyu uchun
        "current_topic": current_topic, # shablonda ishlatyapsan
        "contents": contents,
    })
