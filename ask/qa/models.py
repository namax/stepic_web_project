from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    added_at = models.DateTimeField('date added', null=True)
    rating = models.IntegerField(null=True)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField('date added', null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.question_text
