# Generated by Django 3.1.2 on 2020-10-19 09:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('slug', models.CharField(max_length=150, unique=True)),
                ('image', models.ImageField(upload_to='Slider')),
                ('created_at', models.DateField()),
                ('description', ckeditor.fields.RichTextField()),
                ('status', models.BooleanField(default=0)),
            ],
        ),
    ]
