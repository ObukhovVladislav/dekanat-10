from django.db import models


class Groups(models.Model):
    name = models.CharField(verbose_name='Название группы', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Students(models.Model):
    number_group = models.ForeignKey(Groups, on_delete=models.CASCADE, verbose_name='Номер группы')
    surname = models.TextField(verbose_name='Фамилия студента', blank=True)
    name = models.TextField(verbose_name='Имя студента', blank=True)
    patronymic = models.TextField(verbose_name='Отчество студента', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
