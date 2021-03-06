# Generated by Django 3.2.9 on 2021-11-29 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MyChoice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('beverage', models.CharField(max_length=80)),
                ('size', models.CharField(max_length=80)),
                ('option', models.CharField(max_length=80)),
                ('sugar', models.CharField(max_length=80)),
                ('topping', models.CharField(max_length=80)),
                ('total', models.IntegerField()),
                ('current_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'my_choices',
            },
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('size', models.CharField(max_length=80)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'toppings',
            },
        ),
        migrations.CreateModel(
            name='Beverage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('size', models.CharField(max_length=80)),
                ('price', models.IntegerField()),
                ('rec_sugar', models.IntegerField()),
                ('rec_ice', models.IntegerField()),
                ('is_ice_only', models.BooleanField(default=False)),
                ('menu_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gongchas.category')),
            ],
            options={
                'db_table': 'beverages',
            },
        ),
    ]
