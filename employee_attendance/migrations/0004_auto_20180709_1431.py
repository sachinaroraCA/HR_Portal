# Generated by Django 2.0.5 on 2018-07-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_attendance', '0003_auto_20180709_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(default='applied', max_length=30),
        ),
    ]