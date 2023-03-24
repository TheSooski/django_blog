# Generated by Django 4.1.7 on 2023-03-19 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sell', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sell',
            name='author',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='book_author',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='title',
        ),
        migrations.AddField(
            model_name='sell',
            name='phone',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='sell',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sell',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]