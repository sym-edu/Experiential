from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_protect
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course
from .serializers import UserSerializer,CourseSerializer
from django.http import JsonResponse

# Register View
class RegisterView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

# Login View
@csrf_protect
@api_view(['POST'])
def login_view(request):
    uname = request.data['username']
    pas = request.data['password']
    user = authenticate(request=None, username=uname, password=pas)
    if user is not None:
        login(request, user)
        return Response({"detail": "Logged in successfully."})
    else:
        return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

# Logout View
@api_view(['POST'])
@login_required
def logout_view(request):
    logout(request)
    return Response({"detail": "Logged out successfully."})

# Add Course View
@api_view(['POST'])
@login_required
def add_course_view(request):
    course_name = request.data.get('course_name')
    course_code = request.data.get('course_code')
    course_description = request.data.get('course_description')

    if not all([course_name, course_code]):
        return Response({'error': 'Incomplete data.'}, status=status.HTTP_400_BAD_REQUEST)

    course = Course.objects.create(course_name=course_name, course_code=course_code, course_description=course_description)
    serializer = CourseSerializer(course)

    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def course_list(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)