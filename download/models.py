from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateTimeField('date published')

    def __str__(self):
        return self.name



class Download(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=3000)
    status = models.IntegerField(default=-1)
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.link