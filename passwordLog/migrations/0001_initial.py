# Generated by Django 3.0.5 on 2020-12-17 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckAudioName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passUser', models.CharField(max_length=250)),
                ('audioname', models.CharField(max_length=100)),
                ('url_site', models.CharField(max_length=250)),
                ('datetime', models.CharField(max_length=100)),
            ],
        ),
    ]
