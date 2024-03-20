from django.db import models

class Project(models.Model):
    type = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    image = models.ImageField(upload_to = 'portfolio/images/')
    url = models.URLField(blank = True) # blank is a property that makes this URL optional

    def __str__(self):
       return self.type