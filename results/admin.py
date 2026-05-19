from django.contrib import admin

from .models import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'user',
        'quiz',
        'score',
        'completed_at'
    ]

    list_filter = [
        'quiz',
        'completed_at'
    ]

    search_fields = [
        'user__username',
        'quiz__title'
    ]

    ordering = ['-completed_at']