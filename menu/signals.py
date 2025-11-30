from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_default_menu(sender, **kwargs):
    from .models import Node
    if not Node.objects.exists():
        Node.objects.create(
            menu_name='main_menu',
            label='Root',
            path='/',
            parent=None
        )
        print("Created default root node.")
