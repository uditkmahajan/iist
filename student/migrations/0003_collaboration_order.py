# Generated by Django 3.0.3 on 2021-05-07 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210507_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaboration',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]