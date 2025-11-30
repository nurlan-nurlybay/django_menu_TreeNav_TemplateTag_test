from django.db import models
from django.urls import reverse

class Node(models.Model):
    menu_name = models.CharField(max_length=50) 
    label = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True, 
                               on_delete=models.CASCADE, 
                               related_name='children')

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        if self.path.startswith("http") or self.path.startswith("/"):
            return self.path
        try:
            return reverse(self.path)
        except:
            return self.path
