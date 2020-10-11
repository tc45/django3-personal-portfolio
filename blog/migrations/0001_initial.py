# Generated by Django 3.1.2 on 2020-10-05 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('date', models.DateField(blank=True, null=True)),
                ('body', models.TextField(max_length=30000)),
                ('image', models.ImageField(blank=True, upload_to='blog/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
