
from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('about/', AboutView.as_view()),
    path('home', HomeView.as_view()),
    path('', HomeView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('ironman/', IronManView.as_view()),
    path('scarletwitch/', ScarletWitchView.as_view()),
    path('doctorstrange/', DoctorStrangeView.as_view()),


]