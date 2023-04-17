from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    movie = models.CharField(max_length=50)


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d')