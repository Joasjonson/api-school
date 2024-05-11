# Generated by Django 5.0.4 on 2024-04-24 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_course', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('level', models.CharField(choices=[('B', 'Basic'), ('I', 'Intermediate'), ('A', 'Advanced')], default='B', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('rg', models.CharField(max_length=9)),
                ('cpf', models.CharField(max_length=11)),
                ('birth_date', models.DateField()),
            ],
        ),
    ]
