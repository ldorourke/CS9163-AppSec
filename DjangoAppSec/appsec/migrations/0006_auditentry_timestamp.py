# Generated by Django 2.1.2 on 2018-11-18 23:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appsec', '0005_performspellcheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditentry',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
