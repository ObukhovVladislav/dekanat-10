import mainapp.views as mainapp
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('groups/', mainapp.groups, name='groups'),
    path('group/student/<int:group_pk/', mainapp.students_page, name='students_page'),
    path('group/create', mainapp.create_group, name='create_group')
]
