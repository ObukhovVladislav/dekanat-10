from django.db import models


class Groups(models.Model):
    name = models.CharField(verbose_name='Название группы', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Students(models.Model):
    number_group = models.ForeignKey(Groups, on_delete=models.CASCADE, verbose_name='Номер группы')
    surname = models.TextField(verbose_name='Фамилия студента', blank=True, max_length=30)
    name = models.TextField(verbose_name='Имя студента', blank=True, max_length=30)
    patronymic = models.TextField(verbose_name='Отчество студента', blank=True, max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
