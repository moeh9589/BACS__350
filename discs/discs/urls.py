from django.urls import path
from django.views.generic import TemplateView
from discapp.views import *

urlpatterns = [
    path('', HomeView.as_view()),
    path('home', HomeView.as_view()),
    path('disc', DiscView.as_view()),
    path('editdisc/', DiscEditView.as_view()),
]