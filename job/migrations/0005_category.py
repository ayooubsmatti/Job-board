# Generated by Django 3.2.2 on 2021-05-07 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20210507_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]
