# Generated by Django 3.2.7 on 2021-10-10 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
