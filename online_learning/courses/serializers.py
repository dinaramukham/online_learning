from django.contrib.sites import requests
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Lesson, Courses
from .validators import validator_youtube


class LessonSerializer(serializers.ModelSerializer):
    link_video = serializers.CharField(validators=[validator_youtube])

    class Meta:
        model = Lesson
        fields = '__all__'


class CoursesSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source='lesson_set', many=True)
    count_lesson = SerializerMethodField()
    you_subscribed = SerializerMethodField()

    def get_count_lesson(self, obj):
        return Lesson.objects.filter(course=obj).count()

    def get_you_subscribed(self, obj):
        # обращение к текущему пользователю
        if self.context['request'].user == obj.payment.user:
            return True
        return False

    class Meta:
        model = Courses
        fields = '__all__'
