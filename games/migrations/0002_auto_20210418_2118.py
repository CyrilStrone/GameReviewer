# Generated by Django 3.1.7 on 2021-04-18 18:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='year',
        ),
        migrations.AddField(
            model_name='game',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата выхода'),
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ManyToManyField(to='games.Genre', verbose_name='жанр'),
        ),
        migrations.AlterField(
            model_name='category',
            name='age',
            field=models.CharField(max_length=20, verbose_name='Разрешенный возраст'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Возрастной рейтинг'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата основания'),
        ),
    ]
