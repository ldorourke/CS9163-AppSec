# Generated by Django 2.1.2 on 2018-11-18 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appsec', '0007_auto_20181118_2336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loginattempt',
            old_name='username',
            new_name='uname',
        ),
    ]