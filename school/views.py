from rest_framework import viewsets, generics
from rest_framework import status
from school.models import Course, Student, Registration
from school.serializer import StudentSerializer, StudentSerializerV2, CourseSerializer, RegistrationSerializer, ListRegistrationStudentSerializer, ListStudentRegistrationSerializer
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page



class StudentViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os Estudantes """
    queryset = Student.objects.all()
     
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        else:
            return StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os cursos disponiveis """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status= status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id

            return response
    http_method_names = ['get', 'post', 'put', 'path']
    

class RegistrationViewSet(viewsets.ModelViewSet):
    """ Exibe os alunos matriculados """
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    http_method_names = ['get', 'post']

    @method_decorator(cache_page(30))
    def dispatch(self, *args, **kwargs):                                     # Cache
        return super(RegistrationViewSet, self).dispatch( *args, **kwargs)
    

class ListRegistrationStudent(generics.ListAPIView):
    """ Listando as matriculas dos alunos """
    def get_queryset(self):
        query_set = Registration.objects.filter(student_id=self.kwargs['pk'])
        return query_set
    serializer_class = ListRegistrationStudentSerializer
    
    
class ListStudentsRegistration(generics.ListAPIView):
    """ Listando alunos e alunas matriculados """
    def get_queryset(self):
        query_set = Registration.objects.filter(course_id=self.kwargs['pk'])
        return query_set
    serializer_class = ListStudentRegistrationSerializer
    
    
