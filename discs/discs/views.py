from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from discapp.models import DiscsData
from discapp.models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .workshop import accordion_data, tabs_data


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
class DiscEditView(LoginRequiredMixin, UpdateView):
    model = DiscsData
    template_name = 'disc_edit.html'
    fields = ['brand', 'name']

class DiscDeleteView(DeleteView): # new
    model = DiscsData
    template_name = 'disc_delete.html'
    success_url = reverse_lazy('home')

class AddDiscView(CreateView):
    model = DiscsData
    template_name = "disc_add.html"
    fields = '__all__'

class DiscDetailView(LoginRequiredMixin, DetailView):
    model = DiscsData
    template_name = 'disc_detail.html'
    
class CardView(TemplateView):
    template_name = 'cardview.html'
    
    def get_context_data(self, **kwargs):
        discs = DiscsData.objects.all()
        return {'cards': [
            dict(title="Disc 1:", body="Innova Valkyrie", image=""),
            dict(title="Disc 2:", body="Innova Wriath", image=""),
            dict(title="Disc 3:", body="Innova Ape", image=""),
            
        ]}
    
class AccordionView(TemplateView):
    template_name = 'accordionview.html'
    discs = DiscsData.objects.all()
    def get_context_data(self, **kwargs):
        return dict(accordion=accordion_data())
    
class TabView(TemplateView):
    template_name = 'tabview.html'
    
    def get_context_data(self, **kwargs):
        tabs = tabs_data()
        return dict(title='Tab View', tabs=tabs)
    