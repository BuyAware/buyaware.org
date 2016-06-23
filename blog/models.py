from django.db import models
from django.contrib.auth.models import User


class PostModel(models.Model):    
    '''
    The post is the most basic element of the news page.
    '''

    # Title of the post
    title = models.CharField(max_length = 255)
    
    # content of the post
    body = models.TextField()

    # scheduled date for publication, after this date, if is_validated is set
    # to true, the post will appear on the page.
    pub_date = models.DateField()

    # A post can be put up for moderation before being published
    is_validated = models.BooleanField()
    
    # The author is selected from a list of staff members.
    author = models.ForeignKey(User)
    
    def __str__(self):
        return self.title

    
