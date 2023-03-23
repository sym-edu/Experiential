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
@login_required
@api_view(['POST'])
def add_course(request):
    print(request.data)
    serializer = CourseSerializer(data=request.data)
    print(serializer.is_valid())
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

@api_view(['GET'])
def u_name(request):
    username = request.user.username if request.user.is_authenticated else 'Guest'
    print(username)
    return Response(username)