from django.urls import path, include
from . import views

urlpatterns = [
    path('<slug:language_slug>/', views.language_view, name='language_topic'),

]