# Generated by Django 4.1.7 on 2023-03-11 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_books_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='slug',
            field=models.SlugField(),
        ),
    ]
