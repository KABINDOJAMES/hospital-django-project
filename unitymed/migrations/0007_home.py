# Generated by Django 4.1.1 on 2023-03-02 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unitymed', '0006_aboutus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(blank=True)),
            ],
        ),
    ]
