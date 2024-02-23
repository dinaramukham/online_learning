from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from online_learning.courses.models import Courses, Lesson
from online_learning.users.models import User


# Create your tests here.
class CoursesTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='teatuser@gmail.ru')
        self.user.set_password('test')
        self.user.save()
        #access_token = str(RefreshToken.for_user(self.user).access_token)
        #self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token }')
        self.courses=Courses.objects.create(title='test', content='test')
        self.courses.save()
        self.lesson = Lesson.objects.create(courses=Courses.objects.get(title='test'), title="test", content="test", link_video="https://www.youtube.com/test")
    def test_create_courses(self):
        data = {'tittle': 'Test', 'content': 'test'}
        response = self.client.post('courses/create/', data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_list_courses(self):

        response = self.client.get('courses/list/')
        self.assertEquals(response.status_code, status.HTTP_200_OK,)
