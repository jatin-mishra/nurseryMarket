# Generated by Django 3.1.2 on 2020-10-29 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201028_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
