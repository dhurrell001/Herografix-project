

from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    question_identifier = models.IntegerField(default=0, null=True, blank=True)


    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link answer to user
    answer_text = models.CharField(max_length=200)
    
    answer_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.answer_text






