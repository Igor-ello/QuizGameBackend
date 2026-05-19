from django.db import models
from django.contrib.auth import get_user_model

from quizzes.models import Quiz

User = get_user_model()


class Result(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='results'
    )

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='results'
    )

    score = models.IntegerField()

    completed_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-completed_at']

    def __str__(self):
        return f'{self.user.username} - {self.quiz.title}'