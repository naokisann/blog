# Generated by Django 2.1.5 on 2019-04-03 15:52

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtext',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
