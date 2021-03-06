# Generated by Django 3.2.7 on 2021-10-25 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0004_auto_20211021_0449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('exp_in_company', models.CharField(max_length=10)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empapp.employee')),
            ],
        ),
    ]
