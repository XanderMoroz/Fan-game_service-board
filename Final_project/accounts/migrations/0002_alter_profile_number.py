# Generated by Django 4.1 on 2022-09-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='number',
            field=models.CharField(blank=True, max_length=10, verbose_name='одноразовый код'),
        ),
    ]