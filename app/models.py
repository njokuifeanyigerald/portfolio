from django.db import models

class Work(models.Model):
    picture = models.ImageField()
    name_of_project = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name_of_project