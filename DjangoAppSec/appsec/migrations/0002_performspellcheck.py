# Generated by Django 2.1.2 on 2018-11-18 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsec', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerformSpellCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file_preview', models.CharField(max_length=1024)),
            ],
        ),
    ]
