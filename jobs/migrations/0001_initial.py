# Generated by Django 4.0 on 2021-12-29 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.URLField(default='https://place-hold.it/100x60')),
                ('location', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('employee_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=40)),
                ('picture', models.URLField(default='https://place-hold.it/100x60')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('skills', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('salary_min', models.DecimalField(decimal_places=2, max_digits=20)),
                ('salary_max', models.DecimalField(decimal_places=2, max_digits=20)),
                ('posted', models.DateField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='jobs.company')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='jobs.speciality')),
            ],
        ),
    ]