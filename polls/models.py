from django.db import models


# Create your models here.

class Play(models.Model):
    id = models.IntegerField(max_length=11, primary_key=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return self.content

class TodoModel(models.Model):
    # name = models.CharField(max_length=200)
    id = models.IntegerField(max_length=11, primary_key=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    # def __str__(self):
    #     return self.name
