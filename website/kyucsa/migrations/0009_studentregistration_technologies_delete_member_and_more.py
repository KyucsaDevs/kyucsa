# Generated by Django 4.2.2 on 2023-11-10 13:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyucsa', '0008_memberverification'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=15)),
                ('lastName', models.CharField(max_length=15)),
                ('programme', models.CharField(choices=[('BITC', 'BITC'), ('BIS', 'BIS'), ('BLIS', 'BLIS')], max_length=15)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('academicStatus', models.CharField(choices=[('Continuing', 'Continuing'), ('Graduated', 'Graduated')], max_length=20)),
                ('studentNumber', models.IntegerField()),
                ('enrollmentYear', models.DateField(verbose_name=datetime.datetime(2023, 11, 10, 16, 45, 39, 878152))),
                ('email', models.EmailField(max_length=50)),
                ('mobileNumber', models.IntegerField()),
                ('registeredAt', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tTitle', models.CharField(max_length=200)),
                ('tDescription', models.CharField(max_length=300)),
                ('tPhoto', models.ImageField(null=True, upload_to='technologies/')),
                ('tUrl', models.URLField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.DeleteModel(
            name='memberVerification',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
