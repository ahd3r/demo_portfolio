# Generated by Django 2.1 on 2018-08-19 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180819_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='when',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
