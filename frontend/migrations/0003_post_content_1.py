# Generated by Django 4.0.1 on 2022-01-18 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_alter_post_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_1',
            field=models.TextField(blank=True, null=True),
        ),
    ]