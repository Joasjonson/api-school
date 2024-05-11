
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
import django
django.setup()


import os
import django
import random
from datetime import datetime
from faker import Faker
from django.db import transaction
from validate_docbr import CPF
from school.models import Student, Course, Registration

def create_students(quantity):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantity):
        cpf = CPF()
        name = fake.name()
        rg = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9) ) 
        cpf = cpf.generate()
        birth_date = fake.date_between(start_date='-18y', end_date='today')
        student = Student(name=name, rg=rg, cpf=cpf, birth_date=birth_date)
        student.save()

def create_courses(quantity):
    fake = Faker('pt_BR')
    Faker.seed(10)
    descriptions = ['Python Fundamentals', 'Intermediate Python', 'Advanced Python', 'Python for Data Science', 'Python/React']
    for _ in range(quantity):
        code_course = "{}{}-{}".format(random.choice("ABCDEF"), random.randrange(10, 99),random.randrange(1, 9))
        description = random.choice(descriptions)
        descriptions.remove(description)
        level = random.choice("BIA")
        course = Course(cod_course=code_course, description=description, level=level)
        course.save()

@transaction.atomic
def create_registrations(quantity):
    students = Student.objects.all()
    courses = Course.objects.all()
    for _ in range(quantity):
        student = random.choice(students)
        course = random.choice(courses)
        period = random.choice(['M', 'A', 'N'])
        registration = Registration(student=student, course=course, period=period)
        registration.save()
        

create_students(200)
create_courses(5)
create_registrations(50)
