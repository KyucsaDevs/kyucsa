# Generated by Django 4.2.2 on 2023-11-10 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyucsa', '0011_alter_studentregistration_enrollmentyear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregistration',
            name='academicStatus',
            field=models.CharField(choices=[('Choose', 'Choose...'), ('Continuing', 'Continuing'), ('Graduated', 'Graduated')], default='Choose', max_length=20),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='enrollmentYear',
            field=models.CharField(choices=[('Choose', 'Choose...'), ('2023', '2023'), ('2023', '2023'), ('2023', '2023'), ('2023', '2023'), ('2023', '2023'), ('2023', '2023')], default='Choose', max_length=10),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='gender',
            field=models.CharField(choices=[('Choose', 'Choose...'), ('M', 'Male'), ('F', 'Female')], default='Choose', max_length=10),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='programme',
            field=models.CharField(choices=[('Choose', 'Choose...'), ('BITC', 'BITC'), ('BIS', 'BIS'), ('BLIS', 'BLIS')], default='Choose', max_length=15),
        ),
    ]