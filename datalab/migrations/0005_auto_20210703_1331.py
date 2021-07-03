# Generated by Django 3.0.6 on 2021-07-03 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datalab', '0004_auto_20210702_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='belongs_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='datalab.SharePost'),
        ),
    ]