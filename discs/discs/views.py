from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from discapp.models import DiscsData
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        return{
            'title': 'Learn about disc golf',
            'body': 'Home:',
        }
    
class DiscView(TemplateView):
    template_name = "disc.html"

    def get_context_data(self, **kwargs):
        discs = DiscsData.objects.all()
        return {
            'title': 'Disc Profile',
            'discs': discs,
        }
class DiscEditView(UpdateView):
    model = DiscsData
    template_name = 'disc_edit.html'
    fields = ['name', 'brand']
    
class DiscDeleteView(DeleteView): # new
    model = DiscsData
    template_name = 'disc_delete.html'
    success_url = reverse_lazy('home')
    
class AddDiscView(CreateView):
    model = DiscsData
    template_name = "disc_add.html"
    fields = '__all__'
    
class DiscDetailView(DetailView):
    model = DiscsData
    template_name = 'disc_detail.html'