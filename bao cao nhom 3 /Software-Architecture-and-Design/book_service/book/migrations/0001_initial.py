# Generated by Django 4.1.5 on 2023-04-03 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=100)),
                ('publishAt', models.CharField(max_length=45)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
