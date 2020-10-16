

from django.http import HttpResponse
from django.urls import path


def home_page_view(request):
    return HttpResponse("<h1>World's Simplest Website</h1>")


urlpatterns = [
    path('', home_page_view),
]