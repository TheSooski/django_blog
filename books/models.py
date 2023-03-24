from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
class Books(models.Model):
    title = models.CharField(max_length=100)
    book_author = models.CharField(default="john doe",max_length=100)
    slug = models.SlugField(null=False, unique=True)
    body = models.TextField()
    data = models.DateField(auto_now_add=True)
    thumb = models.ImageField(default="profile.jpg", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.slug = slugify(self.__str__())
        return super().save(*args, **kwargs)

    def __str__(self):
        return (self.title+"_"+self.book_author).replace(" ", "-")

