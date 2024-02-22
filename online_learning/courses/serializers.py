from rest_framework import serializers, generics
from .models import Lesson, Courses
from .validators import validator_youtube


class LessonSerializer(serializers.ModelSerializer):
    #link_video = serializers.CharField(validators=[validator_youtube])

    class Meta:
        model = Lesson
        fields = '__all__'


class CoursesSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source='lesson_set', many=True)
    count_lesson = serializers.SerializerMethodField()
    def get_count_lesson(self, obj):
        return self.objects.lesson.all().count()
    class Meta:
        model = Courses
        fields = '__all__'
