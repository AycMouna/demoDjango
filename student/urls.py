from django.urls import path
from .views import StudentView, student_list

urlpatterns = [
    path('students/', StudentView.as_view(), name='student-view'),
    path('students/list/', student_list, name='student-list'),
]
