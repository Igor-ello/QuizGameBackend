from django.core.management.base import BaseCommand

from quizzes.models import Quiz, Question, Answer


class Command(BaseCommand):

    help = 'Создание стартовых квизов'

    def handle(self, *args, **kwargs):

        if Quiz.objects.exists():
            self.stdout.write(
                self.style.WARNING(
                    'Квизы уже существуют'
                )
            )
            return

        # =========================
        # QUIZ 1
        # =========================

        quiz1 = Quiz.objects.create(
            title='Python Basics',
            description='Базовый квиз по Python'
        )

        q1 = Question.objects.create(
            quiz=quiz1,
            text='Какой тип данных используется для хранения текста?',
            score=1
        )

        Answer.objects.create(
            question=q1,
            text='String',
            is_correct=True
        )

        Answer.objects.create(
            question=q1,
            text='Integer',
            is_correct=False
        )

        Answer.objects.create(
            question=q1,
            text='Boolean',
            is_correct=False
        )

        Answer.objects.create(
            question=q1,
            text='Float',
            is_correct=False
        )

        q2 = Question.objects.create(
            quiz=quiz1,
            text='Какой оператор используется для цикла?',
            score=1
        )

        Answer.objects.create(
            question=q2,
            text='for',
            is_correct=True
        )

        Answer.objects.create(
            question=q2,
            text='switch',
            is_correct=False
        )

        Answer.objects.create(
            question=q2,
            text='case',
            is_correct=False
        )

        Answer.objects.create(
            question=q2,
            text='select',
            is_correct=False
        )

        # =========================
        # QUIZ 2
        # =========================

        quiz2 = Quiz.objects.create(
            title='Android',
            description='Квиз по Android разработке'
        )

        q3 = Question.objects.create(
            quiz=quiz2,
            text='Какой язык основной для Android?',
            score=1
        )

        Answer.objects.create(
            question=q3,
            text='Kotlin',
            is_correct=True
        )

        Answer.objects.create(
            question=q3,
            text='PHP',
            is_correct=False
        )

        Answer.objects.create(
            question=q3,
            text='Python',
            is_correct=False
        )

        Answer.objects.create(
            question=q3,
            text='Go',
            is_correct=False
        )

        q4 = Question.objects.create(
            quiz=quiz2,
            text='Что используется для сетевых запросов?',
            score=1
        )

        Answer.objects.create(
            question=q4,
            text='Retrofit',
            is_correct=True
        )

        Answer.objects.create(
            question=q4,
            text='Photoshop',
            is_correct=False
        )

        Answer.objects.create(
            question=q4,
            text='Blender',
            is_correct=False
        )

        Answer.objects.create(
            question=q4,
            text='Excel',
            is_correct=False
        )

        self.stdout.write(
            self.style.SUCCESS(
                'Стартовые квизы успешно созданы'
            )
        )