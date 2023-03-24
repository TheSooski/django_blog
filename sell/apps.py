from django.apps import AppConfig


class SellConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sell'

    # def ready(self):
    #     # Import models from other apps here
    #     from blog.books.models import Books
