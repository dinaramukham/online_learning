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

    # payment = serializers.PrimaryKeyRelatedField(read_only=True)

    def get_count_lesson(self, obj):
        return obj.lesson_set.count()

    def get_you_subscribed(self, obj):
        # обращение к текущему пользователю
        if self.context['request'].user == obj.user:
            return True
        return False

    class Meta:
        model = Courses
        fields = '__all__'


class CoursesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
