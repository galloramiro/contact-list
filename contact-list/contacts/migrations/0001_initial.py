# Generated by Django 3.0.5 on 2020-08-18 13:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: +999999999. Up to 15 digits allowed.', regex='\\+?1?\\d{9,15}$')])),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='users/pictures/')),
            ],
        ),
    ]