# Generated by Django 2.2 on 2021-05-31 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groups',
            options={'verbose_name': 'Номер группы', 'verbose_name_plural': 'Номера групп'},
        ),
        migrations.AlterModelOptions(
            name='students',
            options={'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
        migrations.RenameField(
            model_name='groups',
            old_name='number',
            new_name='name',
        ),
    ]
