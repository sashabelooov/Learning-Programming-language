from django.urls import path
from .api_views import (
    LanguageList, LanguageDetail,
    TopicList, TopicDetail,
    ContentList, ContentDetail,
)

urlpatterns = [
    path("languages/", LanguageList.as_view(), name="language-list"),
    path("languages/<int:pk>/", LanguageDetail.as_view(), name="language-detail"),

    path("topics/", TopicList.as_view(), name="topic-list"),
    path("topics/<int:pk>/", TopicDetail.as_view(), name="topic-detail"),

    path("contents/", ContentList.as_view(), name="content-list"),
    path("contents/<int:pk>/", ContentDetail.as_view(), name="content-detail"),
]
