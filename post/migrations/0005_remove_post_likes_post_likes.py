# Generated by Django 4.0.4 on 2022-06-06 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_remove_post_liked_post_likes_delete_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True, default=0, verbose_name='like'),
        ),
    ]
