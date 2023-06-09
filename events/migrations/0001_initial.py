# Generated by Django 4.2.1 on 2023-05-24 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='event_images/')),
                ('tagline', models.CharField(max_length=255)),
                ('schedule', models.DateTimeField()),
                ('description', models.TextField()),
                ('moderator', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('sub_category', models.CharField(max_length=255)),
                ('rigor_rank', models.IntegerField()),
            ],
        ),
    ]
