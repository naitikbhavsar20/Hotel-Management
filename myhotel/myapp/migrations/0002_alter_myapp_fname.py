# Generated by Django 4.1.3 on 2022-11-18 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myapp',
            name='fname',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
