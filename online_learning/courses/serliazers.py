from rest_framework import serializers
from .models import Lesson, Courses


class CoursesySerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields='__all__'