# Generated by Django 5.0.4 on 2024-07-08 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videogame',
            name='comments',
            field=models.ManyToManyField(to='blog.comment'),
        ),
    ]