# Generated by Django 3.1.7 on 2021-05-10 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Roles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]