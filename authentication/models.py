from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20, unique=True)
    course_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name
