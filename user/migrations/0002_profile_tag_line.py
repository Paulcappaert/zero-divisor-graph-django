# Generated by Django 2.2.6 on 2019-12-18 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tag_line',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
