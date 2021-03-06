# Generated by Django 2.0.5 on 2018-07-09 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('ca_emp_in_time', models.DateTimeField()),
                ('ca_emp_out_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=30, null=True, unique=True)),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('username', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(max_length=12, null=True)),
                ('dob', models.DateField()),
                ('designation', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_date', models.DateField(auto_now=True)),
                ('type_of_leave', models.CharField(max_length=30, null=True)),
                ('status', models.CharField(default='in progress', max_length=30)),
                ('type_of_transaction', models.CharField(max_length=30, null=True)),
                ('leave_from', models.DateField(null=True)),
                ('leave_to', models.DateField(null=True)),
                ('leave_days', models.IntegerField(null=True)),
                ('from_session', models.CharField(max_length=30, null=True)),
                ('to_session', models.CharField(max_length=30, null=True)),
                ('reason_for_laeve', models.CharField(max_length=100, null=True)),
                ('remarks', models.CharField(max_length=256, null=True)),
                ('grant_expire_date', models.DateField(null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_attendance.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='log_times',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_time', models.DateTimeField()),
                ('out_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_attendance.Employee'),
        ),
    ]
