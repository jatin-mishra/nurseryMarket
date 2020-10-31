# Generated by Django 3.1.2 on 2020-10-30 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Plant', '0002_auto_20201028_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.CharField(max_length=100)),
                ('buyer', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=1)),
                ('status', models.BooleanField(default=False)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plant.plant')),
            ],
        ),
    ]
