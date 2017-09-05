from django.db import models
from first.models import Author
import django.utils.timezone as timezone

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class Blog(models.Model):
    title = models.CharField(max_length=30)
    blog = models.CharField(max_length=32)
    create_time = models.DateTimeField('date created',auto_now_add=True)
    tag = models.CharField(max_length=32)
    author = models.ForeignKey(Author,on_delete=models.DO_NOTHING)

class Record(models.Model):
    date = models.DateTimeField('DATE CREATED',default=timezone.now)
    way = models.CharField(max_length=32)
    strength = models.CharField(max_length=64)
