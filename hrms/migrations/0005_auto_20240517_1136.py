# Generated by Django 2.2.13 on 2024-05-17 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0004_auto_20240517_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp339', max_length=70),
        ),
    ]
