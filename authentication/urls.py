from django.urls import path
from .views import RegisterView, login_view, logout_view, add_course_view, course_list

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('add_course/', add_course_view, name='add_course'),
    path('course_list/', course_list, name='course_list'),
]
