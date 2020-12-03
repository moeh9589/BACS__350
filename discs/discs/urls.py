from django.urls import path
from django.views.generic import TemplateView
from .views import *
from .views import DiscEditView
from django.conf.urls import url
from django.contrib.auth.forms import UserCreationForm
from .views import AccordionView, CardView, TabView


urlpatterns = [
    path('', HomeView.as_view()),
    path('home', HomeView.as_view(), name='home'),
    path('addhero/', AddDiscView.as_view(), name='disc_new'),
    path('disc/<int:pk>/', DiscDetailView.as_view(), name='disc_deatil'),
    path('disc', DiscView.as_view()),
    path('edit/', DiscEditView.as_view()),
    path('disc/<int:pk>/disc_delete/', DiscDeleteView.as_view(),   name='disc_delete'),
    path('card', CardView.as_view(), name='card'),
    path('accordion', AccordionView.as_view(), name='accordion'),
    path('tab', TabView.as_view(), name='tab'),
    
]
