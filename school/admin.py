from django.contrib import admin
from school.models import Student, Course, Registration

class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'birth_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Student, Students)


class Courses(admin.ModelAdmin):
    list_display = ('id', 'cod_course', 'description', 'level')
    list_display_links = ('id', 'cod_course')
    search_fields = ('cod_course',)

admin.site.register(Course, Courses)


class Registrarions(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period')
    list_display_links = ('id',)

admin.site.register(Registration, Registrarions)
