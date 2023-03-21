from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course
# from .serializers import CourseSerializer, UserSerializer, UserLoginSerializer


class RegisterView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        print(request.data)
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        print(email, password, user)
        if user:
            login(request, user)
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout(request):
    logout(request)
    return Response({'detail': 'Logged out successfully.'})


# @login_required
# @api_view(['POST'])
# def addCourse(request):
#     username = request.user.username
#     course_name = request.data.get('course_name')
#     youtube_link = request.data.get('youtube_link')

#     if not all([course_name, youtube_link]):
#         return Response({'error': 'Incomplete data.'}, status=status.HTTP_400_BAD_REQUEST)

#     course = Course.objects.create(username=username, course_name=course_name, youtube_link=youtube_link)
#     serializer = CourseSerializer(course)

#     return Response(serializer.data, status=status.HTTP_201_CREATED)
