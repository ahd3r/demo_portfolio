# Generated by Django 2.1 on 2018-08-19 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180819_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='when',
            field=models.DateTimeField(),
        ),
    ]
