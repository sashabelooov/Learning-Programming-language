from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Language, Topic, Content, Comment, Rating
from .forms import CommentForm, RatingForm
import re

def to_embed_url(url: str) -> str:
    if "youtu.be/" in url:
        match = re.search(r"youtu\.be/([^?]+)", url)
        if match:
            return f"https://www.youtube.com/embed/{match.group(1)}"
    if "watch?v=" in url:
        return url.replace("watch?v=", "embed/")
    return url

def language_view(request, language_slug):
    language = get_object_or_404(Language, slug=language_slug)
    topics = language.topics.filter(parent__isnull=True).order_by("order")

    return render(request, "topic.html", {
        "language": language,
        "topics": topics,
    })



def content_view(request, language_slug, topic_slug):
    language = get_object_or_404(Language, slug=language_slug)
    topics = language.topics.filter(parent__isnull=True).order_by("order")
    current_topic = get_object_or_404(Topic, slug=topic_slug, language=language)
    contents = current_topic.contents.all().order_by("order")
    
    comment_form = CommentForm()
    rating_form = RatingForm()

    if request.method == 'POST':
        if 'text' in request.POST:  # Comment form
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content = contents.first()  # birinchi content ga comment
                if request.user.is_authenticated:
                    comment.user = request.user
                    comment.name = request.user.username
                comment.save()
                return redirect('topic_content', language_slug=language_slug, topic_slug=topic_slug)
        
        elif 'rating' in request.POST:
            if request.user.is_authenticated:
                rating_form = RatingForm(request.POST)
                if rating_form.is_valid():
                    rating = rating_form.save(commit=False)
                    rating.content = contents.first()
                    rating.user = request.user
                    Rating.objects.filter(content=rating.content, user=request.user).delete()
                    rating.save()
                    return redirect('topic_content', language_slug=language_slug, topic_slug=topic_slug)

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
        "comment_form": comment_form,
        "rating_form": rating_form,
    })




# def content_view(request, language_slug, topic_slug):
    language = get_object_or_404(Language, slug=language_slug)
    topics = language.topics.filter(parent__isnull=True).order_by("order")
    current_topic = get_object_or_404(Topic, slug=topic_slug, language=language)
    contents = current_topic.contents.all().order_by("order")
    
    comment_form = CommentForm()
    rating_form = RatingForm()

    if request.method == 'POST':
        if 'text' in request.POST:  # Comment form
            if request.user.is_authenticated:
                comment_form = CommentForm(request.POST)
                if comment_form.is_valid():
                    comment = comment_form.save(commit=False)
                    comment.content = contents.first()  # First content ga comment qo'shamiz
                    comment.user = request.user
                    comment.save()
                    return redirect('topic_content', language_slug=language_slug, topic_slug=topic_slug)
        
        elif 'rating' in request.POST:  # Rating form
            if request.user.is_authenticated:
                rating_form = RatingForm(request.POST)
                if rating_form.is_valid():
                    rating = rating_form.save(commit=False)
                    rating.content = contents.first()  # First content ga rating qo'shamiz
                    rating.user = request.user
                    
                    # Old rating ni o'chirib yangisini saqlaymiz
                    Rating.objects.filter(content=rating.content, user=request.user).delete()
                    rating.save()
                    return redirect('topic_content', language_slug=language_slug, topic_slug=topic_slug)

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
        "comment_form": comment_form,
        "rating_form": rating_form,
    })