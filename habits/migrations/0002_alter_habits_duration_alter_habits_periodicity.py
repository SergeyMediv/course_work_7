# Generated by Django 5.0.7 on 2024-07-24 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habits',
            name='duration',
            field=models.PositiveIntegerField(verbose_name='Время выполнения в секундах'),
        ),
        migrations.AlterField(
            model_name='habits',
            name='periodicity',
            field=models.PositiveIntegerField(default=1, verbose_name='Раз в неделю'),
        ),
    ]
