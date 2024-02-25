from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from online_learning.courses.models import Courses, Lesson
from online_learning.users.models import User


# Create your tests here.
class CoursesTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='teatuser@gmail.ru', is_superuser=True, is_staff=True)
        self.user.set_password('test')

        self.client.force_authenticate(user=self.user)

    def test_create_courses(self):
        data = {'tittle': 'Test', 'content': 'test'}
        response = self.client.post('courses/create/', data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_list_courses(self):
        response = self.client.get('courses/list/')
        self.assertEquals(response.status_code, status.HTTP_200_OK, )

    def test_destroy_courses(self):
        course = Courses.objects.create(user=self.user, title='test course', content='test content')
        # course.save()
        response = self.client.delete(f'courses/delete/{course.id}/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_courses(self):
        course = Courses.objects.create(user=self.user, title='test course', content='test content')
        new_title = "new test"
        response = self.client.patch(f'/lessons/update/{course.id}/', data={"new_title": new_title}, )

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LessonTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='teatuser@gmail.ru', is_superuser=True, is_staff=True)
        self.user.set_password('test')
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        data = {"title": "test", "content": "test", }
        response = self.client.post('courses/create/', data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_list_lesson(self):
        response = self.client.get('courses/list/')
        self.assertEquals(response.status_code, status.HTTP_200_OK, )

    def test_destroy_lesson(self):
        course = Lesson.objects.create(user=self.user,
                                       courses=Courses.objects.get(pk=1),
                                       title='test course',
                                       content='test content', link_video="")
        # course.save()
        response = self.client.delete(f'courses/delete/{course.id}/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_lesson(self):
        course = Lesson.objects.create(user=self.user,
                                       courses=Courses.objects.get(pk=1),
                                       title='test course',
                                       content='test content', link_video="")
        new_title = "new test"
        response = self.client.patch(f'/lessons/update/{course.id}/',
                                     data={"new_title": new_title}, )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
