# Generated by Django 3.0.7 on 2020-06-08 21:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0006_auto_20200608_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='foto',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media/', verbose_name='image'),
            preserve_default=False,
        ),
    ]