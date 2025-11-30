from django.contrib import admin
from .models import Node


class NodeAdmin(admin.ModelAdmin):
    list_display = ["id", "label", "parent", "path", "menu_name"]


admin.site.register(Node, NodeAdmin)
