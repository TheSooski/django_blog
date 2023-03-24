from django.db import models
from django.contrib.auth.models import User
import sys
sys.path.append('/C:/Users/shach/PycharmProjects/django_project/blog')
from books.models import Books

class Sell(models.Model):
    seller = models.ForeignKey(User,default=1, on_delete=models.CASCADE)
    city = models.TextField()
    price = models.IntegerField(default=0)
    phone = models.TextField(default=0)
    data = models.DateField(auto_now_add=True)
    book = models.ForeignKey(Books, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
