from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True,on_delete=models.CASCADE, related_name='children' )
    url = models.CharField(max_length=200)
    name_url = models.CharField(null=True, blank=True,max_length=200)

    def __str__(self):
        return self.name