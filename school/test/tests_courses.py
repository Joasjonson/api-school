from rest_framework import status
from rest_framework.test import APITestCase
from school.models import Course
from django.urls import reverse

class CoursesTestCase(APITestCase):

    def setUp(self):
        self.list_url = '/courses/'

        self.course1 = Course.objects.create(
            cod_course='TCN1', description='Test Course N1', level='B'
        )

        self.course2 = Course.objects.create(
            cod_course='TCN2', description='Test Course N2', level='A'
        )

    def test_request_get_list_courses_authenticated(self):
        """ Test to check if request Get working for authenticated user """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_request_post_create_new_course(self):
        """ Test to check if request POST to create a new course """
        data = {
            'cod_course': 'NTPR',
            'description': 'New Test Post Request',
            'level': 'B'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_request_delete_course(self):
        """ Test to check request delete """
        response = self.client.delete('/courses/5/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


    def test_request_put_update_course(self):
        """ Test to check request PUT """
        data = {
            'cod_course': 'TCN1', 
            'description': 'Test Course N1 Updated', 
            'level': 'A'
        }
        response = self.client.put('/courses/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)