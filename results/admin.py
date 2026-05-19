from django.contrib import admin
from .models import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'user',
        'quiz',
        'score',
        'max_score',
        'created_at'
    ]

    list_filter = [
        'quiz',
        'created_at'
    ]

    search_fields = [
        'user__username',
        'quiz__title'
    ]

    ordering = ['-created_at']