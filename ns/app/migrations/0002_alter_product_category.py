# Generated by Django 4.2.5 on 2023-10-05 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('HDD', 'Hạt dinh dưỡng'), ('RCQ', 'Rau củ quả'), ('TTD', 'Trà thảo dược')], max_length=3),
        ),
    ]
