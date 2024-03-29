# Generated by Django 3.0.6 on 2020-05-16 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200515_1344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_body',
            new_name='post_body_first',
        ),
        migrations.RenameField(
            model_name='subpostcontent',
            old_name='inter_post_content',
            new_name='inter_post_content_one',
        ),
        migrations.AddField(
            model_name='post',
            name='post_body_second',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subpostcontent',
            name='inter_post_content_three',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subpostcontent',
            name='inter_post_content_two',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(to='blog.Comment'),
        ),
    ]
