from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from .models import Discs

class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        return{
            'title': 'Home Page',
            'body': 'Home:',
        }
    
class DiscView(TemplateView):
    template_name = "disc.html"

    def get_context_data(self, **kwargs):
        discs = Discs.objects.all()
        return {
            'title': 'Disc Profile',
            'discs': discs,
        }
class DiscEditView(CreateView):
    template_name = "disc_edit.html"
    model = Discs
    fields = '__all__'