# Generated by Django 2.0.1 on 2018-04-16 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20180416_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='answer_title',
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.CharField(max_length=20, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='response',
            name='user',
            field=models.CharField(max_length=20, verbose_name='User'),
        ),
    ]