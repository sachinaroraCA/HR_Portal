# Generated by Django 2.0.5 on 2018-07-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_attendance', '0015_auto_20180730_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reimbursement',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
