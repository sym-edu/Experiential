from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20, unique=True)
    course_description = models.TextField(blank=True)
    duration = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    ages = models.CharField(max_length=100)
    video_lesson = models.URLField(blank=True, null=True)
    presentation = models.URLField(blank=True, null=True)
    quiz_questions = models.JSONField(blank=True, null=True)
    written_assessment = models.TextField(blank=True, null=True)
    oral_assessment = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name

class QuizQuestion(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()

    def __str__(self):
        return self.question_text

class QuizOption(models.Model):
    question = models.ForeignKey(QuizQuestion, related_name='options', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
