# Generated by Django 2.2.12 on 2021-04-07 06:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('event_id', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('email1', models.TextField()),
                ('email2', models.TextField()),
                ('email3', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='delevent',
            name='description',
            field=models.TextField(default="desc", max_length=200),
            preserve_default=False
        ),
        migrations.AddField(
            model_name='delevent',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 6, 22, 28, 934625, tzinfo=utc)),
            preserve_default=False
        ),
        migrations.AddField(
            model_name='delevent',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 6, 22, 40, 255057, tzinfo=utc)),
            preserve_default=False
        ),
        migrations.AddField(
            model_name='delevent',
            name='title',
            field=models.CharField(default='title', max_length=200),
            preserve_default=False
        ),
    ]
