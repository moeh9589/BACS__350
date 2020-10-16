from django.test import TestCase

# Create your tests here.

from .models import heros

class HeroTests(TestCase):
    
    def test_hero_model(self):
        self.assertEqual(len(Superhero.objects.all()), 0)
        
    def test_create(self):
        heros.objects.create(name='Hulk', identity='Bruce Banner')
        self.assertEqual(len(Superhero.objects.all()), 1)
        self. assertEqual(Superhero.objects.get(pk=1).name, 'Hulk')
        self. assertEqual(Superhero.objects.get(pk=1).identity, 'Bruce Banner')
        
    def test_update(self):
        heros.objects.create(name='Hulk', identity='Bruce Banner')
        x = Superhero.objects.get(pk=1)
        x.name = 'Iron Man'
        x.save()
        y = Superhero.objects.get(pk=1)
        self. assertEqual(y.name, 'Iron Man')
        self. assertEqual(y.identity, 'Bruce Banner')
        
    def test_read(self):
        heros.objects.create(name='Hulk', identity='Bruce Banner')
        x = Superhero.objects.get(pk=1)
        self. assertEqual(x.name, 'Hulk')
        self. assertEqual(x.identity, 'Bruce Banner')
        
    def test_image(self):
        heros.objects.create(name='Hulk', identity='Bruce Banner')
        x = Superhero.objects.get(pk=1)
        x.image = 'Hulk.jpg'
        x.save()
        self. assertEqual(x.image, 'Hulk.jpg')