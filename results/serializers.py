from rest_framework import serializers

from .models import Result


class ResultSerializer(serializers.ModelSerializer):

    quiz_title = serializers.CharField(
        source='quiz.title',
        read_only=True
    )

    class Meta:
        model = Result
        fields = [
            'id',
            'quiz',
            'quiz_title',
            'score',
            'completed_at'
        ]

        read_only_fields = ['completed_at']