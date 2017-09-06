from django.db import models
from first.models import Author
from datetime import datetime
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
    date = models.DateTimeField(default=timezone.now,verbose_name='记录时间')
    way = models.CharField(max_length=32,verbose_name="运动方式")
    strength = models.CharField(max_length=64,verbose_name="强度")
    class Meta():
        verbose_name="记录"
        verbose_name_plural="记录"

    def __str__(self):
        return '%s-%s-%s-%s'%(self.way,self.date.year,self.date.month,self.date.day)
