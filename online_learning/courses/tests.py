from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from online_learning.courses.models import Courses, Lesson
from online_learning.users.models import User, Subscription


# Create your tests here.
class CoursesTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='teatuser@gmail.ru', is_superuser=True, is_staff=True)
        self.user.set_password('testtesttest')

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

    def test_post_courses(self):
        """
            проверка обновления подписки
        """
        course_item = Courses.objects.create(user=self.user, title='test course', content='test content')
        subs_item = Subscription.objects.filter(user=self.user, courses=course_item)
        if subs_item.exists():
            subs_item.delete()
            data = 'подписка удалена'
        else:
            Subscription.objects.create(user=self.user, courses=course_item)
            data = 'подписка добавлена'

        response = self.client.patch('subscription/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LessonTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='teatuser@gmail.ru', is_superuser=True, is_staff=True)
        self.user.set_password('testtesttest')
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        data = {"title": "test", "content": "test", }
        response = self.client.post('lessons/create/', data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_list_lesson(self):
        response = self.client.get('lessons/list/')
        self.assertEquals(response.status_code, status.HTTP_200_OK, )

    def test_destroy_lesson(self):
        lesson = Lesson.objects.create(user=self.user,
                                       courses=Courses.objects.get(pk=1),
                                       title='test course',
                                       content='test content',
                                       link_video="https://www.youtube.com/test")
        # course.save()
        response = self.client.delete(f'lessons/delete/{lesson.id}/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_lesson(self):
        lesson = Lesson.objects.create(user=self.user,
                                       courses=Courses.objects.get(pk=1),
                                       title='test course',
                                       content='test content',
                                       link_video="https://www.youtube.com/test")
        new_title = "new test"
        response = self.client.patch(f'/lessons/update/{lesson.id}/',
                                     data={"new_title": new_title}, )

        self.assertEqual(response.status_code, status.HTTP_200_OK)