# Generated by Django 3.1.5 on 2021-04-06 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vacations', '0009_auto_20210406_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='profile_pic',
            field=models.ImageField(default='/media/df.png', upload_to=''),
        ),
    ]
