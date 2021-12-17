# Generated by Django 3.2.9 on 2021-12-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gongchas', '0008_auto_20211206_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('beverage', models.CharField(max_length=80)),
                ('size', models.CharField(max_length=80)),
                ('option', models.CharField(max_length=80)),
                ('sugar', models.CharField(max_length=80)),
                ('ice', models.CharField(max_length=80)),
                ('topping', models.CharField(blank=True, max_length=80, null=True)),
                ('total', models.IntegerField(default=0)),
                ('current_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'receipt',
            },
        ),
    ]