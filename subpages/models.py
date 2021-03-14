from django.db import models
import datetime
from django.conf import settings

# Create your models here.


class memes(models.Model):
    author = models.ForeignKey(
                        settings.AUTH_USER_MODEL,
                        on_delete=models.CASCADE,
                        related_name = 'meme_posts',
                        )
    title = models.TextField(max_length=100)
    post_data = models.FileField(upload_to='memes')
    created_on = models.DateTimeField(auto_now_add = True)



    def __str__(self):
        return '{} by {}'.format(self.title, self.author)


class confessions(models.Model):
    title = models.CharField(max_length=100)
    post_data = models.TextField(max_length=5000)
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '{} on {}'.format(self.title, self.created_on)

class examCorner(models.Model):
    author = models.ForeignKey(
                        settings.AUTH_USER_MODEL,
                        on_delete=models.CASCADE,
                        related_name = 'examCorner_post',
                        )
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=5000)                    
    post_data = models.FileField(upload_to='ExamCorner', blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return '{} by {}'.format(self.title, self.author)


class WebDevelopment(models.Model):
    author = models.ForeignKey(
                        settings.AUTH_USER_MODEL,
                        on_delete=models.CASCADE,
                        related_name = 'webdev_post',
                        )
    title = models.TextField(max_length=100)                    
    description = models.TextField(max_length=5000)                    
    created_on = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return '{} by {}'.format(self.title, self.author)


class ml(models.Model):
    author = models.ForeignKey(
                        settings.AUTH_USER_MODEL,
                        on_delete=models.CASCADE,
                        related_name = 'ml_post',
                        )
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=5000)                    
    created_on = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return '{} by {}'.format(self.title, self.author)
