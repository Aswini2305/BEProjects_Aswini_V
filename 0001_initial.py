# Generated by Django 3.1.4 on 2020-12-23 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('options1', models.CharField(max_length=100)),
                ('options2', models.CharField(max_length=100)),
                ('options3', models.CharField(max_length=100)),
                ('options4', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
    ]
