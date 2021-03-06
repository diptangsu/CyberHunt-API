# Generated by Django 2.2.1 on 2019-05-09 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='dept1',
            field=models.CharField(default='CSE', max_length=10),
        ),
        migrations.AddField(
            model_name='team',
            name='dept2',
            field=models.CharField(default='CSE', max_length=10),
        ),
        migrations.AddField(
            model_name='team',
            name='name1',
            field=models.CharField(default='John Doe', max_length=50),
        ),
        migrations.AddField(
            model_name='team',
            name='name2',
            field=models.CharField(default='Jane Doe', max_length=50),
        ),
        migrations.AddField(
            model_name='team',
            name='password',
            field=models.CharField(default='password', max_length=20),
        ),
        migrations.AddField(
            model_name='team',
            name='phone1',
            field=models.BigIntegerField(default=1234),
        ),
        migrations.AddField(
            model_name='team',
            name='phone2',
            field=models.BigIntegerField(default=1234),
        ),
        migrations.AddField(
            model_name='team',
            name='year1',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='team',
            name='year2',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='team',
            name='teamname',
            field=models.CharField(default='Team', max_length=20),
        ),
    ]
