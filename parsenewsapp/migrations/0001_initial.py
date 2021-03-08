# Generated by Django 3.1.7 on 2021-03-08 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockNewsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('title', models.CharField(max_length=100)),
                ('article', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
