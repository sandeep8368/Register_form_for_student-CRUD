# Generated by Django 5.0.1 on 2024-04-02 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='Pasword',
            new_name='Password',
        ),
    ]