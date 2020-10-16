from django.shortcuts import render
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name="page.html"
    def get_context_data(self, **kwargs):
        return{
            'title': 'About Page',
            'body': 'about page',
        }
    
class HomeView(TemplateView):
    template_name="about.html"
    def get_context_data(self, **kwargs):
        return{
            'title': 'Home',
            'info': 'Learn about my favorite superheroes!',
            
        }
    
class ProfileView(TemplateView):
    template_name="page.html"
    def get_context_data(self, **kwargs):
        return{
            'title': 'Title',
            'body': 'body',
        }
    
class HeroView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        id = kwargs.get('identity', 'Ironman')
        return{'hero' : id}
    
class IronManView(TemplateView):
    template_name="home.html"
    def get_context_data(self, **kwargs):
        return{
            'title': 'Iron Man',
            'info': 'Iron man is one of the original Avengers. Played by Robert Downey Jr in the movies.',
            'otherHero': 'Scarlet Witch',
            'otherHeroUrl': 'scarletwitch',
            'otherHero1': 'Doctor Strange',
            'otherHero1Url': 'doctorstrange',
        }
class ScarletWitchView(TemplateView):
    template_name="home.html"
    def get_context_data(self, **kwargs):
        return{
            'name': 'Scarlet Witch',
            'identity': 'Wanda Maximoff',
            'title': 'Scarlet Witch',
            'info': 'Scarlet Witch, also known as Wanda Maximoff, is the twin of Pietro Maximoff. She is played by Elizabeth Olsen in the movies.',
            'otherHero': 'Iron Man',
            'otherHeroUrl': 'ironman',
            'otherHero1': 'Doctor Strange',
            'otherHeroUrl1': 'doctorstrange',
        }
class DoctorStrangeView(TemplateView):
    template_name="home.html"
    def get_context_data(self, **kwargs):
        return{
            'title': 'Doctor Strange',
            'info': 'Doctor Strange found magical powers after a car accident left his career of surgery in shambles. He is played by Benedict Cumberpatch in the movies.',
            'otherHero': 'Iron Man',
            'otherHeroUrl': 'ironman',
            'otherHero1': 'Scarlet Witch',
            'otherHero1Url': 'scarletwitch',
        }
