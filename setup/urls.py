
from django.contrib import admin
from django.urls import path, include
from school.views import CourseViewSet, StudentViewSet, RegistrationViewSet, ListRegistrationStudent, ListStudentsRegistration
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

route = routers.DefaultRouter()
route.register('students', StudentViewSet, basename='student')
route.register('courses', CourseViewSet, basename='course')
route.register('registrations', RegistrationViewSet, basename='registration')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls) ),
    path('students/<int:pk>/registrations/', ListRegistrationStudent.as_view()),
    path('courses/<int:pk>/registrations/', ListStudentsRegistration.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

