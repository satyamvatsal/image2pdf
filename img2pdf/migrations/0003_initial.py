# Generated by Django 4.2.11 on 2024-06-18 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('img2pdf', '0002_delete_image_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameUser', models.CharField(max_length=100)),
            ],
        ),
    ]
