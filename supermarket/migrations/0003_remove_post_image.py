# Generated by Django 3.0.5 on 2020-05-29 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0002_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
