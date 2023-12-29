from django.contrib import admin
from .models import Course , Registration, Mark




class CourseAdmin(admin.ModelAdmin):

    list_display= ('name','teacher','class_quantity')
    list_filter = ('teacher',)


admin.site.register(Course,CourseAdmin)

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('course','student')
    list_filter = ('course','student')



admin.site.register(Registration,RegistrationAdmin)
# Register your models here.




class MarkAdmin(admin.ModelAdmin):
    list_display = ('course','student','mark_1','average')
    list_filter = ('course',)
admin.site.register(Mark,MarkAdmin)