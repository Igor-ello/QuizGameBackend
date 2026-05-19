from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Result
from .serializers import ResultSerializer


class ResultCreateView(generics.CreateAPIView):

    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        quiz = serializer.validated_data['quiz']

        max_score = sum(q.score for q in quiz.questions.all())

        serializer.save(
            user=self.request.user,
            max_score=max_score
        )


class MyResultsView(generics.ListAPIView):

    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Result.objects.filter(user=self.request.user)