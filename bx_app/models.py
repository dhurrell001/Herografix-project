

from django.db import models
from django.contrib.auth.models import User
from django import forms

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link answer to user
    answer_text = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date answered')

    def __str__(self):
        return self.answer_text






