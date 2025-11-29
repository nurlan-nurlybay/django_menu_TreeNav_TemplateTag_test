from django.db import models


class Node(models.Model):
    label = models.CharField(max_length=200)
    parent = models.ForeignKey('self', 
                               null=True, 
                               blank=True, 
                               on_delete=models.CASCADE,
                               related_name='children')
    path = models.CharField(max_length=200)
    
    def __str__(self):
        return self.label
    