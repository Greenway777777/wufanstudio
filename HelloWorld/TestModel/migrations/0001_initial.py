# Generated by Django 2.2.7 on 2019-11-22 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestmodelPressinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
            options={
                'db_table': 'testModel_pressinfo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TestmodelUserinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'testModel_userinfo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TestmodelBookinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('pub_date', models.DateField()),
                ('author', models.ManyToManyField(to='TestModel.TestmodelUserinfo')),
                ('press', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestModel.TestmodelPressinfo')),
            ],
            options={
                'db_table': 'testModel_bookinfo',
                'managed': True,
            },
        ),
    ]
