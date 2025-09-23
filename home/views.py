from django.shortcuts import render
from course.models import Language

def home(request):
    languages = Language.objects.all()
    return render(request, "home.html", {
        "languages": languages,
            
    })