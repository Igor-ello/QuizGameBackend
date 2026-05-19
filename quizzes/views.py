from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Quiz
from .serializers import QuizSerializer


class QuizListView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]


class QuizDetailView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]