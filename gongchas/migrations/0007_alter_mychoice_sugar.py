# Generated by Django 3.2.9 on 2021-12-01 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gongchas', '0006_auto_20211201_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mychoice',
            name='sugar',
            field=models.CharField(max_length=80),
        ),
    ]
