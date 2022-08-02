# Generated by Django 3.2 on 2022-08-02 13:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ani', '0002_rename_ani_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付'),
        ),
        migrations.AddField(
            model_name='day',
            name='text',
            field=models.TextField(default='入力必須', max_length=2000, verbose_name='本文'),
            preserve_default=False,
        ),
    ]