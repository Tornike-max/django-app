# Generated by Django 5.0 on 2023-12-09 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('max_pages', models.IntegerField(default=240)),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
    ]