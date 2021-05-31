# Generated by Django 2.2 on 2021-05-31 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=128, verbose_name='Номер группы')),
            ],
            options={
                'verbose_name': 'Номера групп',
                'verbose_name_plural': 'Номер группы',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.TextField(blank=True, verbose_name='Фамилия студента')),
                ('name', models.TextField(blank=True, verbose_name='Имя студента')),
                ('patronymic', models.TextField(blank=True, verbose_name='Отчество студента')),
                ('number_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Groups')),
            ],
            options={
                'verbose_name': 'Студенты',
                'verbose_name_plural': 'Студент',
            },
        ),
    ]
