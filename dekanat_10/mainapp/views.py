from django.shortcuts import render

from mainapp.models import Groups, Students


def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'mainapp/index.html', context)


def groups(request):
    group = Groups.objects.all()
    context = {
        'group': group,
        'page_title': 'Группы'
    }
    return render(request, 'mainapp/groups.html', context)


def students_page(request, group_pk):
    student = Students.objects.filter(group_id=group_pk)
    context = {
        'student': student,
        'page_title': 'Студенты'
    }
    return render(request, 'mainapp/students_page.html', context)


def create_group():
    pass


def edit_group():
    pass
