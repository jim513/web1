# Generated by Django 3.0.4 on 2021-01-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20210121_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
