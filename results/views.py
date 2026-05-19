from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Result
from .serializers import ResultSerializer


class ResultCreateView(generics.CreateAPIView):

    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MyResultsView(generics.ListAPIView):

    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Result.objects.filter(
            user=self.request.user
        )