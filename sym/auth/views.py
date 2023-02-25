from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer

class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response_data = {
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            },
            "message": "User registered successfully."
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    print(username,password)
    if user is not None:
        login(request, user)
        response = JsonResponse({'message': 'Logged in successfully'})
        response['session_key'] = request.session.session_key
        return response
    else:
        return JsonResponse({'message': 'Invalid credentials'})

@login_required
def restricted_view(request):
    data = {'message': 'This is a restricted view'}
    return JsonResponse(data)
