from django.urls import path
from .views import RegisterView, login_view, logout_view, add_course, get_courses, u_name, get_user_details,chat

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('add_course/', add_course, name='add_course'),
    path('course_list/', get_courses, name='course_list'),
    path('user/', u_name, name='user'),
    path('user_deets/', get_user_details, name='user_deets'),
    path('/chat', chat , name='chat')
    
]
