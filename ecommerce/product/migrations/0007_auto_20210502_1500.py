# Generated by Django 3.1.7 on 2021-05-02 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210502_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image4',
        ),
    ]