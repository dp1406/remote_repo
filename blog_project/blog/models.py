from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    STATUS_CHOICES=(("draft","Draft"),('publish','Publish'))
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=264,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_post', on_delete = models.CASCADE)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')


    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_datail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])







