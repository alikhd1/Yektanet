# Generated by Django 3.1.6 on 2021-02-08 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('advertising', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='advertiser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.advertiser', verbose_name='تبلیغ دهنده'),
        ),
    ]
