# Generated by Django 2.1.2 on 2018-11-18 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsec', '0002_performspellcheck'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='performspellcheck',
            name='created_at',
            field=models.CharField(max_length=128),
        ),
    ]