# Generated by Django 5.0.1 on 2024-04-02 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Email_id', models.CharField(max_length=50)),
                ('Pasword', models.CharField(max_length=50)),
                ('Phone_No', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=10)),
                ('Area_of_Interest', models.CharField(max_length=100)),
            ],
        ),
    ]
