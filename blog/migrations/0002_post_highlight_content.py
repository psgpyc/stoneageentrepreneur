# Generated by Django 3.0.6 on 2020-05-15 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='highlight_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
