# Generated by Django 4.2.8 on 2023-12-08 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptno', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='salgrade',
            fields=[
                ('grade', models.IntegerField(primary_key=True, serialize=False)),
                ('lowsal', models.IntegerField()),
                ('highsal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('mgr', models.CharField(max_length=100)),
                ('hiredate', models.DateField()),
                ('salary', models.IntegerField()),
                ('comm', models.IntegerField()),
                ('deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
        migrations.CreateModel(
            name='bonus',
            fields=[
                ('job', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('sal', models.IntegerField()),
                ('comm', models.IntegerField()),
                ('ename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
            ],
        ),
    ]
