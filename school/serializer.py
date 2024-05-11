from rest_framework import serializers
from school.models import Student, Course, Registration

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'cpf', 'birth_date', 'image']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'cod_course', 'description', 'level']


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration            # Bring wich DataBase
        fields = '__all__'              # Bring all de fields

class ListRegistrationStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Registration
        fields = ['course', 'period']

    def get_period(self, obj):
        return obj.get_period_display()


class ListStudentRegistrationSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    class Meta:
        model = Registration
        fields = ['student_name']



class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'phone', 'rg', 'cpf', 'birth_date', 'image']




