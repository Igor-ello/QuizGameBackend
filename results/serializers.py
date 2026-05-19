from rest_framework import serializers
from .models import Result


class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = [
            'id',
            'user',
            'quiz',
            'score',
            'max_score',
            'created_at'
        ]
        read_only_fields = ['created_at', 'user']   