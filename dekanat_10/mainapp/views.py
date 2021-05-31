from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from mainapp.models import Groups, Students
from django.urls import reverse

from mainapp.forms import GroupsForm


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


def create_group(request):
    if request.method == 'POST':
        form = GroupsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:groups'))
    else:
        form = GroupsForm()
    context = {
        'title': 'Добавить группу',
        'form': form,
    }
    return render(request, 'mainapp/add_group.html', context)


def edit_group():
    pass
