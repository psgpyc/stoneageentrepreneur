# Generated by Django 3.0.6 on 2020-05-15 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200515_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listelements',
            name='sub_elements',
        ),
        migrations.RemoveField(
            model_name='subpostlistelements',
            name='li_element',
        ),
        migrations.AddField(
            model_name='listelements',
            name='belongs_to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.SubPostListElements'),
            preserve_default=False,
        ),
    ]
