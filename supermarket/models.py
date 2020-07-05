from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from  django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image1 = models.ImageField(default='sld4.jpg', upload_to='profile_pics')
    firstname = models.TextField(default='name')
    lastname = models.TextField(default='name')
    phonenumber =  models.IntegerField(default='0712345678')
    message = models.TextField(default='place message')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

