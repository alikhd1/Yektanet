# Generated by Django 3.1.6 on 2021-02-02 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertising', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='clicks',
            field=models.IntegerField(default=0, verbose_name='کلیک ها'),
        ),
        migrations.AddField(
            model_name='ad',
            name='views',
            field=models.IntegerField(default=0, verbose_name='بازدید ها'),
        ),
    ]