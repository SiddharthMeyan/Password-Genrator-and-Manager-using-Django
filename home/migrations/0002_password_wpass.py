# Generated by Django 3.1.3 on 2021-01-28 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='password',
            name='wpass',
            field=models.CharField(default='l', max_length=100),
        ),
    ]