# Generated by Django 3.2.7 on 2021-10-21 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0003_alter_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.FileField(default='/profile/my.jpg', upload_to='profile/'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='leave_status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], max_length=20),
        ),
    ]
