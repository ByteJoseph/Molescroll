# Generated by Django 4.2.7 on 2023-12-26 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.CharField(max_length=25000000000),
        ),
        migrations.AlterField(
            model_name='posts',
            name='message',
            field=models.TextField(max_length=2500000000000),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=2500000000000),
        ),
    ]
