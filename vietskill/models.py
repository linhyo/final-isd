from django.db import models
from datetime import datetime


class StaffProfile(models.Model):
    name = models.CharField(max_length=128)
    birthday = models.DateField()
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    position = models.CharField(max_length=128)
    email = models.EmailField()
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=11)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.name
"""
    def age(self):
        today = date.today()
        return today.year - StaffProfile.birthday.year
"""


class Statistic(models.Model):
    staff = models.ForeignKey(StaffProfile)
    num_teaching_days = models.IntegerField()
    days_off = models.IntegerField()
    num_mistakes = models.IntegerField()


class Meeting(models.Model):
    date_time = models.DateTimeField(default=datetime.now, blank=True)
    purpose = models.TextField()
    location = models.CharField(max_length=100)
    note = models.TextField()


class MeetingPaticipant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    staff_id = models.IntegerField(default=-1, blank=True)
    meeting = models.ForeignKey(Meeting)


class Plan(models.Model):
    start_date = models.DateField()
    due_date = models.DateField()
    duration = models.IntegerField()
    content = models.TextField()
    STATUS_CHOICES = (
        ('1', 'Completed'),
        ('2', 'In Progress'),
        ('3', 'New')
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    staffs = models.ManyToManyField(StaffProfile)


class Event(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    location = models.CharField(max_length=100)


class TeachingSchedule(models.Model):
    staff = models.ForeignKey(StaffProfile)
    DAY_CHOICES = (
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday')
    )
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    SESSION_CHOICES = (
        ('1', '7:15 - 9:00'),
        ('2', '9:30 - 11:15'),
        ('3', '12:30 - 14:15'),
        ('4', '14:45 - 16:30')
    )
    session = models.CharField(max_length=1, choices=SESSION_CHOICES)
    SUBJECT_CHOICES = (
        ('1', 'Master of Ceremonies'),
        ('2', 'Life Skill'),
        ('3', 'Art'),
        ('4', 'Soft Skill'),
        ('5', 'Copy Editing'),
        ('6', 'Communication'),
        ('7', 'Culture'),
        ('8', 'Marketing'),
        ('9', 'Presentation'),
    )
    subject = models.CharField(max_length=1, choices=SUBJECT_CHOICES)
    classes = models.CharField(max_length=20)
    room = models.CharField(max_length=10)

    def __repr__(self):
        return "<ScheduleItem day: %r session: %r>" % (self.day, self.session)

    @property
    def get_subject(self):
        if self.subject:
            return dict(TeachingSchedule.SUBJECT_CHOICES)[self.subject]
        else:
            return ""

    @property
    def get_session(self):
        if self.session:
            return dict(TeachingSchedule.SESSION_CHOICES)[self.session]
        else:
            return ""

    @property
    def get_day(self):
        if self.day:
            return dict(TeachingSchedule.DAY_CHOICES)[self.day]
        else:
            return ""


class StaffShift(models.Model):
    staff = models.ForeignKey(StaffProfile)
    date = models.DateField()
    time = models.CharField(max_length=30)
    num_shift = models.IntegerField()
    location = models.CharField(max_length=100)


class Assessment(models.Model):
    staff = models.ForeignKey(StaffProfile)
    content = models.TextField()
    date = models.DateField()
    assess_point = models.IntegerField()

    def __str__(self):
        return self.content


class Recruitment(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    release_date = models.DateField()
    expiry_date = models.DateField()
    office = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.title
