# Generated by Django 3.0.6 on 2020-05-16 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200516_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, to='blog.Comment'),
        ),
    ]