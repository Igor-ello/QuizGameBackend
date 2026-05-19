from django.urls import path

from .views import (
    ResultCreateView,
    MyResultsView
)

urlpatterns = [
    path(
        '',
        ResultCreateView.as_view(),
        name='create-result'
    ),

    path(
        'my/',
        MyResultsView.as_view(),
        name='my-results'
    ),
]