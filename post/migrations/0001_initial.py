# Generated by Django 4.2.7 on 2024-01-27 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=3000)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='post/media/images/')),
            ],
        ),
    ]
