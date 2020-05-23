# Generated by Django 3.0.6 on 2020-05-19 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200516_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='listelements',
            name='element_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='subpostcontent',
            name='inter_post_content_one_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='subpostcontent',
            name='inter_post_content_three_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='subpostcontent',
            name='inter_post_content_two_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='subpostlistelements',
            name='title_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
