# Generated by Django 5.0.7 on 2024-07-18 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='vote',
            new_name='votes',
        ),
    ]