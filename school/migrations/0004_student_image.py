# Generated by Django 5.0.4 on 2024-05-07 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
