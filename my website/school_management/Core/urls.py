from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('classes/', views.classes, name='classes'),
    path('subjects/', views.subjects, name='subjects'),
    path('attendance/', views.attendance, name='attendance'),
    path('grades/', views.grades, name='grades'),
    path('announcements/', views.announcements, name='announcements'),
]