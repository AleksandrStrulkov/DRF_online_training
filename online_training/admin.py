from django.contrib import admin
from online_training.models import Course, Lesson, Payments


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ('title', 'preview', 'description', 'owner')
	list_filter = ('title',)
	search_fields = ('title', 'description',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
	list_display = ('title', 'preview', 'description', 'video', 'course', 'owner')
	list_filter = ('title',)
	search_fields = ('title', 'description',)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
	list_display = ('user', 'date_payment', 'payment_course', 'payment_amount', 'payment_method')
	list_filter = ('payment_course',)


