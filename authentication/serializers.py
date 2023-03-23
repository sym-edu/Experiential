from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Course, QuizQuestion, QuizOption


class QuizOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizOption
        fields = ('id', 'answer_text', 'is_correct')

class QuizQuestionSerializer(serializers.ModelSerializer):
    options = QuizOptionSerializer(many=True)

    class Meta:
        model = QuizQuestion
        fields = ('id', 'question_text', 'options')

class CourseSerializer(serializers.ModelSerializer):
    quiz_questions = QuizQuestionSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'course_name', 'course_code', 'course_description', 'duration', 'cost', 'ages', 'video_lesson',
                  'presentation', 'quiz_questions', 'written_assessment', 'oral_assessment')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
