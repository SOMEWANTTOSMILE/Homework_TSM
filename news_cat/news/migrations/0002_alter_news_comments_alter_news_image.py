# Generated by Django 5.0.1 on 2024-02-01 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='comments',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/news/img'),
        ),
    ]
