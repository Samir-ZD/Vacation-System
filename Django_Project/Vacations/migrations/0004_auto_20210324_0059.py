# Generated by Django 3.1.5 on 2021-03-23 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vacations', '0003_auto_20210315_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='profile_pic',
            field=models.ImageField(default='static/images/df.png', upload_to=''),
        ),
    ]
