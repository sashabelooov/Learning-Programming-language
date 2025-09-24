from django.shortcuts import render, get_object_or_404
from django.shortcuts import get_object_or_404
from .models import Language, Topic, Content
import re


def language_view(request, language_slug):
    language = get_object_or_404(Language, slug=language_slug)
    topics = language.topics.all().order_by("order")

    return render(request, "topic.html", {
        "language": language,
        "topics": topics,
    })



def to_embed_url(url: str) -> str:
    """YouTube linkni embed formatga aylantiradi"""
    if "youtu.be/" in url:
        match = re.search(r"youtu\.be/([^?]+)", url)
        if match:
            return f"https://www.youtube.com/embed/{match.group(1)}"
    if "watch?v=" in url:
        return url.replace("watch?v=", "embed/")
    return url  # agar allaqachon embed bo'lsa



def content_view(request, language_slug, topic_slug):
    language = get_object_or_404(Language, slug=language_slug)
    topics = language.topics.all().order_by("order")
    current_topic = get_object_or_404(Topic, slug=topic_slug, language=language)
    contents = current_topic.contents.all().order_by("order")

    # Har bir content uchun video_url ni to'g'rilaymiz
    for c in contents:
        if c.video_url:
            c.embed_url = to_embed_url(c.video_url)
        else:
            c.embed_url = None

    return render(request, "content.html", {
        "language": language,
        "topics": topics,
        "current_topic": current_topic,
        "contents": contents,
    })