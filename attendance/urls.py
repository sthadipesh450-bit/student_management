from django.urls import path

from .views import (
    AttendanceListView,
    AttendanceCreateView,
    AttendanceUpdateView,
    AttendanceDeleteView
)


urlpatterns = [

    path(
        '',
        AttendanceListView.as_view(),
        name='attendance_list'
    ),

    path(
        'add/',
        AttendanceCreateView.as_view(),
        name='attendance_add'
    ),

    path(
        'edit/<int:pk>/',
        AttendanceUpdateView.as_view(),
        name='attendance_edit'
    ),

    path(
        'delete/<int:pk>/',
        AttendanceDeleteView.as_view(),
        name='attendance_delete'
    ),
]