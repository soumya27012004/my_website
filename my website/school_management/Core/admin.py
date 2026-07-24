from django.contrib import admin
from .models import Student, Teacher, SchoolClass, Subject, Attendance, Grade, Announcement

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(SchoolClass)
admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(Grade)
admin.site.register(Announcement)