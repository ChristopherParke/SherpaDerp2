# Generated by Django 2.2.4 on 2019-09-01 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0006_auto_20190901_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
