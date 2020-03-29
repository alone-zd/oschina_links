# Generated by Django 2.0 on 2020-03-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OsChina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('links', models.CharField(max_length=500, verbose_name='链接')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
            ],
            options={
                'db_table': 'urls',
            },
        ),
    ]