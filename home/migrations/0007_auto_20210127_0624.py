# Generated by Django 3.1.5 on 2021-01-27 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_video_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ('-published_at',)},
        ),
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]