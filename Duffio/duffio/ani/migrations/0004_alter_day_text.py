# Generated by Django 3.2 on 2022-08-02 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ani', '0003_auto_20220802_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='text',
            field=models.TextField(verbose_name='本文'),
        ),
    ]