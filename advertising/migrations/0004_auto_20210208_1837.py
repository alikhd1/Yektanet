# Generated by Django 3.1.6 on 2021-02-08 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertising', '0003_eventtracking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtracking',
            name='event',
            field=models.CharField(choices=[('ck', 'click'), ('vi', 'view')], max_length=2, verbose_name='نوع رویداد'),
        ),
    ]
