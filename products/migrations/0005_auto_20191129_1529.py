# Generated by Django 2.2.7 on 2019-11-29 14:29
from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0004_auto_20191129_1256'),
    ]

    operations = [
        TrigramExtension(),
    ]