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

