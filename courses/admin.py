from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'instructor')

admin.site.register(Course, CourseAdmin)