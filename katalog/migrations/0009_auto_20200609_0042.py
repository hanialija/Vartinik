# Generated by Django 3.0.7 on 2020-06-08 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0008_auto_20200609_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='qmimi',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
