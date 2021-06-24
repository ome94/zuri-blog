from django.db import models

# Create your models here.
class Post(models.Model):

    """
    The Post Model is a table of stories, news, articles, gists, etc, on the blog.
    
    * The `title` is the headline.
    
    * The table should have ONE & ONLY ONE Post AS A MAJOR STORY FOR THE SITE HEADLINE.
    * Therefore there should be a mechanism for unsetting the previous major story post as a major story,
      whenever another post is set a major story.

    * Each post should have a timestamp to keep track of the latest articles.


    """

    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()

    # 

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()