from django.db import models 


class Student(models.Model):
    name = models.CharField(max_length=40)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()
    phone = models.CharField(max_length=11, default="")
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
    

class Course(models.Model):
    LEVEL = (
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    )
    cod_course = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.description
    

class Registration(models.Model):
    PERIOD = (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('N', 'Night')
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(max_length=1, choices=PERIOD, blank=False, default='M')
    
    