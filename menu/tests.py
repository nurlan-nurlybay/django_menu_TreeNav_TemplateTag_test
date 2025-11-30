from django.test import TestCase
from django.template import Context, Template
from .models import Node

class MenuTagTest(TestCase):
    def setUp(self):
        self.root = Node.objects.create(menu_name='main_menu', label='Root', path='/root/')
        self.child1 = Node.objects.create(menu_name='main_menu', label='Child 1', path='/root/child1/', parent=self.root)
        self.grandchild1 = Node.objects.create(menu_name='main_menu', label='Grandchild 1', path='/root/child1/gc1/', parent=self.child1)

    def test_draw_menu_renders(self):
        template = Template("{% load menu_tags %}{% draw_menu 'main_menu' %}")
        context = Context({'request': None})
        rendered = template.render(context)
        
        self.assertNotIn('Root', rendered)
        self.assertIn('Child 1', rendered)
        
    def test_draw_menu_expanded(self):
        from django.test import RequestFactory
        factory = RequestFactory()
        request = factory.get('/root/child1/')
        
        template = Template("{% load menu_tags %}{% draw_menu 'main_menu' %}")
        context = Context({'request': request})
        rendered = template.render(context)
        
        self.assertNotIn('Root', rendered)
        self.assertIn('Child 1', rendered)
        self.assertIn('Grandchild 1', rendered)
