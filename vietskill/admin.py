from django.contrib import admin
from vietskill.models import StaffProfile, Meeting, Plan, Event, TeachingSchedule, Recruitment, Assessment


class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'sex', 'position', 'email', 'address', 'phone_number', 'picture')


class MeetingAdmin(admin.ModelAdmin):
    list_display = ('purpose', 'date_time', 'location')


class PlanAdmin(admin.ModelAdmin):
    list_display = ('content', 'status', 'start_date', 'due_date', 'duration')


class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'content', 'location')


class TeachingScheduleAdmin(admin.ModelAdmin):
    list_display = ('staff', 'subject', 'day', 'session', 'classes', 'room')


class RecruitmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'release_date', 'expiry_date', 'office', 'position')


class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('staff', 'content', 'date', 'assess_point')

admin.site.register(StaffProfile, StaffProfileAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(TeachingSchedule, TeachingScheduleAdmin)
admin.site.register(Recruitment, RecruitmentAdmin)
admin.site.register(Assessment, AssessmentAdmin)
