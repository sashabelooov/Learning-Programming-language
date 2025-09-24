from django.urls import path, include
from . import views

urlpatterns = [
    path('<slug:language_slug>/', views.language_view, name='language_topic'),
    path('<slug:language_slug>/<slug:topic_slug>/', views.content_view, name='topic_content'),
]