from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from quizzes.models import Quiz, Question, Answer, Tag

User = get_user_model()


class Command(BaseCommand):

    help = "Создание тестовых квизов (5 штук)"

    def handle(self, *args, **kwargs):

        # очищаем старые данные (чтобы не дублировалось)
        Answer.objects.all().delete()
        Question.objects.all().delete()
        Quiz.objects.all().delete()
        Tag.objects.all().delete()

        user = User.objects.first()

        if not user:
            self.stdout.write(self.style.ERROR("Нет пользователей. Создай superuser"))
            return

        # =========================
        # ТЕГИ
        # =========================
        python_tag = Tag.objects.create(name="Python")
        android_tag = Tag.objects.create(name="Android")
        backend_tag = Tag.objects.create(name="Backend")
        django_tag = Tag.objects.create(name="Django")
        general_tag = Tag.objects.create(name="General")

        # =========================
        # QUIZ 1
        # =========================
        quiz1 = Quiz.objects.create(
            title="Python Basics",
            description="Базовый квиз по Python",
            author=user
        )
        quiz1.tags.add(python_tag, general_tag)

        q1 = Question.objects.create(
            quiz=quiz1,
            text="Какой тип данных используется для текста?",
            score=1
        )
        Answer.objects.bulk_create([
            Answer(question=q1, text="str", is_correct=True),
            Answer(question=q1, text="int", is_correct=False),
            Answer(question=q1, text="bool", is_correct=False),
            Answer(question=q1, text="float", is_correct=False),
        ])

        q2 = Question.objects.create(
            quiz=quiz1,
            text="Какой цикл в Python?",
            score=1
        )
        Answer.objects.bulk_create([
            Answer(question=q2, text="for", is_correct=True),
            Answer(question=q2, text="foreach", is_correct=False),
            Answer(question=q2, text="loop", is_correct=False),
            Answer(question=q2, text="repeat", is_correct=False),
        ])

        # =========================
        # QUIZ 2
        # =========================
        quiz2 = Quiz.objects.create(
            title="Android Basics",
            description="Основы Android разработки",
            author=user
        )
        quiz2.tags.add(android_tag)

        q3 = Question.objects.create(
            quiz=quiz2,
            text="Основной язык Android?",
            score=1
        )
        Answer.objects.bulk_create([
            Answer(question=q3, text="Kotlin", is_correct=True),
            Answer(question=q3, text="Swift", is_correct=False),
            Answer(question=q3, text="Python", is_correct=False),
            Answer(question=q3, text="PHP", is_correct=False),
        ])

        q4 = Question.objects.create(
            quiz=quiz2,
            text="Что используется для UI?",
            score=1
        )
        Answer.objects.bulk_create([
            Answer(question=q4, text="XML Layout", is_correct=True),
            Answer(question=q4, text="HTML", is_correct=False),
            Answer(question=q4, text="CSS", is_correct=False),
            Answer(question=q4, text="JSON", is_correct=False),
        ])

        # =========================
        # QUIZ 3
        # =========================
        quiz3 = Quiz.objects.create(
            title="Django Fundamentals",
            description="Основы Django",
            author=user
        )
        quiz3.tags.add(django_tag, backend_tag)

        q5 = Question.objects.create(
            quiz=quiz3,
            text="Как называется ORM Django?",
            score=1
        )
        Answer.objects.bulk_create([
            Answer(question=q5, text="Django ORM", is_correct=True),
            Answer(question=q5, text="SQLAlchemy", is_correct=False),
            Answer(question=q5, text="Hibernate", is_correct=False),
            Answer(question=q5, text="Sequelize", is_correct=False),
        ])

        q6 = Question.objects.create(
            quiz=quiz3,
            text="Что такое Django?",
            score=1
        )
        Answer.objects.bulk_create([
            Answer(question=q6, text="Web framework", is_correct=True),
            Answer(question=q6, text="Database", is_correct=False),
            Answer(question=q6, text="OS", is_correct=False),
            Answer(question=q6, text="IDE", is_correct=False),
        ])

        # =========================
        # QUIZ 4
        # =========================
        quiz4 = Quiz.objects.create(
            title="Backend Basics",
            description="Основы backend разработки",
            author=user
        )
        quiz4.tags.add(backend_tag, general_tag)

        q7 = Question.objects.create(
            quiz=quiz4,
            text="Что такое API?",
            score=1
        )
        Answer.objects.bulk_create([
            Answer(question=q7, text="Interface for communication", is_correct=True),
            Answer(question=q7, text="Database", is_correct=False),
            Answer(question=q7, text="Server", is_correct=False),
            Answer(question=q7, text="Frontend", is_correct=False),
        ])

        q8 = Question.objects.create(
            quiz=quiz4,
            text="Какой протокол чаще всего используется?",
            score=1
        )
        Answer.objects.bulk_create([
            Answer(question=q8, text="HTTP", is_correct=True),
            Answer(question=q8, text="FTP", is_correct=False),
            Answer(question=q8, text="SMTP", is_correct=False),
            Answer(question=q8, text="SSH", is_correct=False),
        ])

        # =========================
        # QUIZ 5
        # =========================
        quiz5 = Quiz.objects.create(
            title="General Knowledge",
            description="Общий квиз",
            author=user
        )
        quiz5.tags.add(general_tag)

        q9 = Question.objects.create(
            quiz=quiz5,
            text="Столица Франции?",
            score=1
        )
        Answer.objects.bulk_create([
            Answer(question=q9, text="Paris", is_correct=True),
            Answer(question=q9, text="London", is_correct=False),
            Answer(question=q9, text="Berlin", is_correct=False),
            Answer(question=q9, text="Madrid", is_correct=False),
        ])

        q10 = Question.objects.create(
            quiz=quiz5,
            text="Сколько планет в Солнечной системе?",
            score=1
        )
        Answer.objects.bulk_create([
            Answer(question=q10, text="8", is_correct=True),
            Answer(question=q10, text="9", is_correct=False),
            Answer(question=q10, text="7", is_correct=False),
            Answer(question=q10, text="10", is_correct=False),
        ])

        self.stdout.write(self.style.SUCCESS("5 квизов успешно созданы"))