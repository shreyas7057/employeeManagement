# Generated by Django 3.2.7 on 2021-10-10 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0002_alter_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.FileField(default='/media/profile/my.jpg', upload_to='profile/'),
        ),
    ]