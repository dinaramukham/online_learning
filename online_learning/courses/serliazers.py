
from rest_framework import serializers, generics
from .models import Lesson, Courses


class CoursesySerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields='__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lesson
        fields='__all__'

