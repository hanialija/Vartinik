# Generated by Django 3.0.3 on 2020-06-04 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='qmimi',
            field=models.IntegerField(null=True),
        ),
    ]