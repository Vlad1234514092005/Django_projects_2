from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.IntegerField()
    publishing_date = models.IntegerField()
    genre = models.CharField(max_length=255)
    description = models.TextField()
    is_published_on_website = False

    def publish(self):
        self.is_published_on_website = True
        self.save()

    def __str__(self):
        return self.title
