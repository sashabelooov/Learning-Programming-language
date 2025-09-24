from django.shortcuts import render
from course.models import Language
from django.utils.translation import gettext as _


def home(request):
    languages = Language.objects.all()
    return render(request, "home.html", {
        "languages": languages,
            
    })