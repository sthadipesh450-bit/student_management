from django.urls import path

from .views import (
    ResultListView,
    ResultDetailView,
    ResultCreateView,
    ResultUpdateView,
    ResultDeleteView
)


urlpatterns = [

    path(
        '',
        ResultListView.as_view(),
        name='result_list'
    ),

    path(
        'add/',
        ResultCreateView.as_view(),
        name='result_add'
    ),

    path(
        '<int:pk>/',
        ResultDetailView.as_view(),
        name='result_detail'
    ),

    path(
        '<int:pk>/edit/',
        ResultUpdateView.as_view(),
        name='result_edit'
    ),

    path(
        '<int:pk>/delete/',
        ResultDeleteView.as_view(),
        name='result_delete'
    ),
]