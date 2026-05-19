from rest_framework import serializers
from .models import Quiz, Question, Answer, Tag


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'text', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):

    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'score', 'answers']


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name']


class QuizSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(many=True, required=False)
    tags = TagSerializer(many=True, required=False)
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Quiz
        fields = [
            'id',
            'title',
            'description',
            'author',
            'author_username',
            'tags',
            'questions',
            'created_at'
        ]
        read_only_fields = ['author', 'created_at']

    def create(self, validated_data):

        validated_data.pop('author', None)

        tags_data = validated_data.pop('tags', [])
        questions_data = validated_data.pop('questions', [])

        quiz = Quiz.objects.create(
            author=self.context['request'].user,
            **validated_data
        )

        for tag in tags_data:
            tag_obj, _ = Tag.objects.get_or_create(**tag)
            quiz.tags.add(tag_obj)

        for q_data in questions_data:
            answers_data = q_data.pop('answers', [])

            question = Question.objects.create(
                quiz=quiz,
                **q_data
            )

            for a_data in answers_data:
                Answer.objects.create(
                    question=question,
                    **a_data
                )

        return quiz