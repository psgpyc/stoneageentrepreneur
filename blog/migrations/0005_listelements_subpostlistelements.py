# Generated by Django 3.0.6 on 2020-05-15 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_delete_subpostlistelements'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListElements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Category Created Date')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Category Updated Date')),
                ('is_active', models.BooleanField(default=True)),
                ('elements', models.CharField(max_length=1000)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('sub_elements', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.ListElements')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubPostListElements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Category Created Date')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Category Updated Date')),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.SubPostContent')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('li_element', models.ForeignKey(max_length=1000, on_delete=django.db.models.deletion.CASCADE, to='blog.ListElements')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
