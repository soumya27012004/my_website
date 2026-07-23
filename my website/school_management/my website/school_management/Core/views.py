from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Teacher, SchoolClass, Subject, Attendance, Grade, Announcement
from datetime import date

def dashboard(request):
    today = date.today()
    total = Attendance.objects.filter(date=today).count()
    present = Attendance.objects.filter(date=today, status='present').count()
    rate = round((present / total) * 100) if total > 0 else 0
    context = {
        'total_students': Student.objects.count(),
        'total_teachers': Teacher.objects.count(),
        'total_classes': SchoolClass.objects.count(),
        'total_subjects': Subject.objects.count(),
        'present_today': present,
        'absent_today': Attendance.objects.filter(date=today, status='absent').count(),
        'attendance_rate': rate,
        'announcements': Announcement.objects.order_by('-created_at')[:5],
    }
    return render(request, 'dashboard.html', context)

def students(request):
    return render(request, 'students.html', {
        'students': Student.objects.select_related('school_class').order_by('-created_at')
    })

def teachers(request):
    return render(request, 'teachers.html', {
        'teachers': Teacher.objects.all().order_by('-created_at')
    })

def classes(request):
    return render(request, 'classes.html', {
        'classes': SchoolClass.objects.select_related('teacher').all()
    })

def subjects(request):
    return render(request, 'subjects.html', {
        'subjects': Subject.objects.select_related('teacher', 'school_class').all()
    })

def attendance(request):
    filter_date = request.GET.get('date', str(date.today()))
    records = Attendance.objects.filter(date=filter_date).select_related('student', 'school_class')
    return render(request, 'attendance.html', {
        'records': records,
        'filter_date': filter_date,
        'present': records.filter(status='present').count(),
        'absent': records.filter(status='absent').count(),
        'late': records.filter(status='late').count(),
    })

def grades(request):
    return render(request, 'grades.html', {
        'grades': Grade.objects.select_related('student', 'subject').order_by('-created_at')
    })

def announcements(request):
    return render(request, 'announcements.html', {
        'announcements': Announcement.objects.order_by('-created_at')
    })