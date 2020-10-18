from django.urls import path
from django.views.generic import TemplateView
from .views import *
from .views import DiscEditView

urlpatterns = [
    path('', HomeView.as_view()),
    path('home', HomeView.as_view()),
    path('addhero/', AddDiscView.as_view(), name='disc_new'),
    path('post/<int:pk>/', DiscDetailView.as_view(), name='disc_deatil'),
    path('disc', DiscView.as_view()),
    path('/edit/', DiscEditView.as_view()),
    path('disc_delete/', DiscDeleteView.as_view(),   name='disc_delete/')
]