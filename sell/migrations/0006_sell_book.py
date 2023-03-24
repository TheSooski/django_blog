# Generated by Django 4.1.7 on 2023-03-24 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_books_slug'),
        ('sell', '0005_remove_sell_book_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='books.books'),
        ),
    ]
