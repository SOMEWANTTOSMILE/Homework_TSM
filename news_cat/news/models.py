from django.db import models


class News(models.Model):
    image = models.ImageField(upload_to='static/news/img', blank=True, null=True)
    title = models.CharField(max_length=128, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)
    comments = models.TextField(null=True)

    def __str__(self):
        return f'{self.title} {self.content} {self.likes} {self.dislikes} {self.rating} {self.date} {self.views}'


class Comment(models.Model):
    nick_name = models.CharField(max_length=128)
    content = models.TextField(max_length=255)
    date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    news = models.ForeignKey('News', on_delete=models.CASCADE, related_name='comments_news')