from django.contrib import admin

from .models import Quiz, Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title']
    ordering = ['-created_at']
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'quiz', 'score']
    list_filter = ['quiz']
    search_fields = ['text']
    inlines = [AnswerInline]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'question', 'is_correct']
    list_filter = ['is_correct']
    search_fields = ['text']