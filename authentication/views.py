from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_protect,csrf_exempt
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
@csrf_exempt
# @login_required
@api_view(['POST'])
def add_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Get All Courses View
@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data, status=200)

# @api_view(['POST'])
# def add_course_details(request):
    try:
        course = Course.objects.get(course_code=request.data.get('code'))
    except Course.DoesNotExist:
        return Response({'error': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)

    video_link = request.data.get('video_link')
    presentation_link = request.data.get('presentation_link')
    quiz_questions = request.data.get('quiz_questions')
    written_assessment = request.data.get('written_assessment')
    oral_assessment = request.data.get('oral_assessment')

    if not any([video_link, presentation_link, quiz_questions, written_assessment, oral_assessment]):
        return Response({'error': 'No course details provided.'}, status=status.HTTP_400_BAD_REQUEST)

    course.video_link = video_link
    course.presentation_link = presentation_link
    course.quiz_questions = quiz_questions
    course.written_assessment = written_assessment
    course.oral_assessment = oral_assessment

    course.save()
    serializer = CourseSerializer(course)

    return Response(serializer.data, status=status.HTTP_200_OK)



# @api_view(['GET'])
# def course_list(request):
#     courses = Course.objects.all()
#     serializer = CourseSerializer(courses, many=True)
#     return Response(serializer.data)