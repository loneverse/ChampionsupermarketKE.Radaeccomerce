# Generated by Django 3.0.5 on 2020-07-05 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0004_post_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='firstname',
            field=models.TextField(default='name'),
        ),
        migrations.AddField(
            model_name='post',
            name='lastname',
            field=models.TextField(default='name'),
        ),
        migrations.AddField(
            model_name='post',
            name='message',
            field=models.TextField(default='place message'),
        ),
        migrations.AddField(
            model_name='post',
            name='phonenumber',
            field=models.IntegerField(default='0712345678'),
        ),
    ]
