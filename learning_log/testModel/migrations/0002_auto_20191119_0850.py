# Generated by Django 2.2.7 on 2019-11-19 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testModel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='idpassword',
            field=models.CharField(max_length=19, unique=True),
        ),
    ]
