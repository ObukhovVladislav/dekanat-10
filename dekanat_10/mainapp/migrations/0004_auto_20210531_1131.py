# Generated by Django 2.2 on 2021-05-31 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210531_1109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groups',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterField(
            model_name='groups',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Название группы'),
        ),
    ]