from django.shortcuts import render, get_object_or_404
from .models import Language



def language_view(request, language_slug):
    language = get_object_or_404(Language, slug=language_slug)
    topics = language.topics.all().order_by("order")
    print(f"topics:{topics}")
    return render(request, "topic.html", {
        "language": language,
        "topics": topics,
    })
