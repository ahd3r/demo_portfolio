# Generated by Django 2.1 on 2018-08-19 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20180819_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='when',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
