# Generated by Django 2.1 on 2018-08-19 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180819_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='when',
            field=models.DateField(auto_now=True),
        ),
    ]