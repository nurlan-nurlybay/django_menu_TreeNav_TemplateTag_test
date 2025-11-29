from django.contrib import admin
from .models import Node


class NodeAdmin(admin.ModelAdmin):
    # ...
    list_display = ["id", "label", "parent", "path"]


admin.site.register(Node, NodeAdmin)
