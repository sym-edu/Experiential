from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Course


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            # email=validated_data['email'],
            username=validated_data['username']
        )
        # print(validated_data['email'],validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'course_name', 'youtube_link', 'username')