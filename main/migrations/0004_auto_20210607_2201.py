# Generated by Django 3.2.4 on 2021-06-08 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210607_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='conseil',
            name='q10',
            field=models.CharField(default='<any>', editable=False, max_length=1024),
        ),
        migrations.AddField(
            model_name='conseil',
            name='q7',
            field=models.CharField(default='<any>', editable=False, max_length=1024),
        ),
        migrations.AddField(
            model_name='conseil',
            name='q8',
            field=models.CharField(default='<any>', editable=False, max_length=1024),
        ),
        migrations.AddField(
            model_name='conseil',
            name='q9',
            field=models.CharField(default='<any>', editable=False, max_length=1024),
        ),
        migrations.AddField(
            model_name='randomuser',
            name='q10',
            field=models.CharField(default='skip', editable=False, max_length=1024),
        ),
        migrations.AddField(
            model_name='randomuser',
            name='q7',
            field=models.CharField(default='skip', editable=False, max_length=1024),
        ),
        migrations.AddField(
            model_name='randomuser',
            name='q8',
            field=models.CharField(default='skip', editable=False, max_length=1024),
        ),
        migrations.AddField(
            model_name='randomuser',
            name='q9',
            field=models.CharField(default='skip', editable=False, max_length=1024),
        ),
    ]
